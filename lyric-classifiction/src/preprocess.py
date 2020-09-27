import re
from dataclasses import asdict, dataclass
from typing import List

import joblib
import pandas as pd
from bs4 import BeautifulSoup

from src.const import DataPath
from src.zenhan import (
    ASCII_HANKAKU_CHARS,
    ASCII_ZENKAKU_CHARS,
    DIGIT_HANKAKU_CHARS,
    DIGIT_ZENKAKU_CHARS,
)


@dataclass
class TitleLyric:
    title: str = None
    lyric: str = None


class Preprocesssor:
    def _clean_lyric(self, s: str) -> str:
        s_ = (
            s.replace('<p id="Lyric">', "")
            .replace("</p>", "")
            .replace("<br/><br/>", "<br/>")
            .replace("<br/>", "。")
            .replace(" ", "、")
            .replace("\u3000", "、")
        )
        for han, zen in zip(ASCII_HANKAKU_CHARS, ASCII_ZENKAKU_CHARS):
            s_ = re.sub(zen, han, s_)
        for han, zen in zip(DIGIT_HANKAKU_CHARS, DIGIT_ZENKAKU_CHARS):
            s_ = re.sub(zen, han, s_)
        return s_

    def _extract_title(self, page_source: str) -> str:
        soup = BeautifulSoup(page_source, "html.parser")
        title = soup.find("h2").text.split("\xa0")[0]
        return title

    def _extract_lyric(self, page_source: str) -> str:
        soup = BeautifulSoup(page_source, "html.parser")
        lyric = str(soup.find("p", id="Lyric"))
        lyric = self._clean_lyric(lyric)
        return lyric

    def _load(self, path: str) -> List[str]:
        lyrics: List[str] = joblib.load(path)
        return lyrics

    def _preprocess(self, path: str) -> List[TitleLyric]:
        sources = self._load(path)
        title_lyric_list: List[TitleLyric] = []
        for source in sources:
            title = self._extract_title(source)
            lyric = self._extract_lyric(source)
            tl = TitleLyric()
            tl.title = title
            tl.lyric = lyric
            title_lyric_list.append(tl)
        return title_lyric_list

    def run(self):
        for name in DataPath.raw.__annotations__.keys():
            title_lyric_list = self._preprocess(getattr(DataPath.raw, name))
            df = pd.DataFrame([asdict(x) for x in title_lyric_list])
            joblib.dump(df, getattr(DataPath.interim, name), compress=3)

        df_andymori = joblib.load(getattr(DataPath.interim, "andymori"))
        df_andymori["label"] = "oyamada"
        df_nagasawa = joblib.load(getattr(DataPath.interim, "nagasawa"))
        df_nagasawa["label"] = "nagasawa"
        df_train = pd.concat((df_andymori, df_nagasawa), axis=0, ignore_index=True)
        joblib.dump(df_train, DataPath.processed.train, compress=3)

        df_al = joblib.load(getattr(DataPath.interim, "al"))
        joblib.dump(df_al, DataPath.processed.test, compress=3)
