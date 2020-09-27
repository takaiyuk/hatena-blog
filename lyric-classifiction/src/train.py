from dataclasses import asdict, dataclass
from typing import List

import joblib
import lightgbm as lgb
import numpy as np
import pandas as pd
from janome.analyzer import Analyzer
from janome.tokenfilter import POSStopFilter
from janome.tokenizer import Tokenizer
from sklearn.decomposition import TruncatedSVD
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

from src.const import DataPath


@dataclass
class ProcessedData:
    train: pd.DataFrame
    test: pd.DataFrame


@dataclass
class TrainData:
    X_train: pd.DataFrame
    y_train: np.array
    X_valid: pd.DataFrame
    y_valid: np.array
    X_test: pd.DataFrame


class Trainer:
    def _load(self) -> ProcessedData:
        train: pd.DataFrame = joblib.load(DataPath.processed.train)
        test: pd.DataFrame = joblib.load(DataPath.processed.test)
        return ProcessedData(train=train, test=test)

    def _tokenize(self, ProcessedData: ProcessedData) -> ProcessedData:
        train = ProcessedData.train
        test = ProcessedData.test

        tokenizer = Tokenizer()
        token_filters = [POSStopFilter(["記号", "助詞", "助動詞"])]
        analyzer = Analyzer(tokenizer=tokenizer, token_filters=token_filters)

        word_separations = []
        for i in range(len(train)):
            tokens = analyzer.analyze(train["lyric"].values[i])
            word_separations.append(" ".join([t.surface for t in tokens]))
        train["word_separation"] = word_separations

        word_separations = []
        for i in range(len(test)):
            tokens = analyzer.analyze(test["lyric"].values[i])
            word_separations.append(" ".join([t.surface for t in tokens]))
        test["word_separation"] = word_separations

        return ProcessedData(train=train, test=test)

    def _vectorize(
        self, ProcessedData: ProcessedData, n_components: int = 32
    ) -> ProcessedData:
        train = ProcessedData.train
        test = ProcessedData.test

        vectorizer = TfidfVectorizer(ngram_range=(1, 2), dtype=np.float32)
        X = vectorizer.fit_transform(train["word_separation"].values)
        X_test = vectorizer.transform(test["word_separation"].values)
        train["bow"] = [bow for bow in X.toarray()]
        test["bow"] = [bow for bow in X_test.toarray()]

        svd = TruncatedSVD(n_components=n_components, random_state=42)
        svd_ = svd.fit_transform(X)
        svd_test = svd.transform(X_test)
        for i in range(n_components):
            train[f"svd_{i}"] = svd_[:, i]
            test[f"svd_{i}"] = svd_test[:, i]

        return ProcessedData(train=train, test=test)

    def _train(self, ProcessedData: ProcessedData) -> TrainData:
        train = ProcessedData.train
        test = ProcessedData.test

        svd_cols = [col for col in train.columns if col.startswith("svd_")]
        X_train, X_valid, y_train, y_valid = train_test_split(
            train.loc[:, svd_cols], train["label"], test_size=0.3, random_state=42
        )
        X_test = test.loc[:, svd_cols]
        y_train = np.array([0 if y == "oyamada" else 1 for y in y_train])
        y_valid = np.array([0 if y == "oyamada" else 1 for y in y_valid])

        params = {
            "learning_rate": 0.1,
            "num_leaves": 31,
            "max_depth": -1,
            "feature_fraction": 1.0,
            "bagging_fraction": 1.0,
            "bagging_freq": 5,
            "seed": 42,
        }
        model = lgb.LGBMClassifier(**params)
        model.fit(
            X_train,
            y_train,
            eval_set=[(X_train, y_train), (X_valid, y_valid)],
            early_stopping_rounds=20,
            verbose=20,
        )
        pred_valid = model.predict(X_valid)
        pred_test = model.predict(X_test)
        score = accuracy_score(y_valid, pred_valid)
        print(f"accuracy: {score}\t{np.sum(y_valid == pred_valid)}/{len(pred_valid)}")

        X_valid["pred"] = ["oyamada" if p == 0 else "nagasawa" for p in pred_valid]
        X_valid = X_valid.loc[:, ["pred"]].join(
            train.loc[:, ["title", "label"]], how="left"
        )
        X_test["pred"] = ["oyamada" if p == 0 else "nagasawa" for p in pred_test]
        X_test = X_test.loc[:, ["pred"]].join(test.loc[:, ["title"]], how="left")

        return TrainData(
            X_train=X_train,
            y_train=y_train,
            X_valid=X_valid,
            y_valid=y_valid,
            X_test=X_test,
        )

    def run(self):
        data = self._load()
        data = self._tokenize(data)
        data = self._vectorize(data, n_components=32)
        result = self._train(data)
        joblib.dump(result, "./result.jbl", compress=3)
