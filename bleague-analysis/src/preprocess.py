from typing import Dict, List, Union

import pandas as pd


def aggregate(
    df: pd.DataFrame, key: Union[str, List[str]], agg_dict: Dict[str, List[str]]
) -> pd.DataFrame:
    for v in agg_dict.values():
        assert type(v) == list
    df_agg = df.groupby(key).agg(agg_dict).round(2)
    df_agg.columns = [f"{c[0]}_{c[1]}" for c in df_agg.columns]
    df_agg = df_agg.reset_index()
    return df_agg
