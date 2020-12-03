import io
import os

import pandas as pd
import requests


def load(url: str, overwrite: bool = False) -> pd.DataFrame:
    data_prefix = "./data"
    # notebooks 以下での実行時に data_prefix を変更する
    if os.path.basename(os.getcwd()) == "notebooks":
        data_prefix = f".{data_prefix}"
    os.makedirs(data_prefix, exist_ok=True)
    data_path = f"{data_prefix}/{os.path.basename(url)}"
    # ローカルにデータがないときだけgithubからデータをロードする
    if not os.path.exists(data_path) or overwrite:
        print(f"Load from {url}")
        r = requests.get(url)
        df = pd.read_csv(io.BytesIO(r.content), sep=",")
        df.to_csv(data_path, index=False)
    else:
        df = pd.read_csv(data_path)
    return df
