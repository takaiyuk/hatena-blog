from typing import Dict, List, Tuple, Union

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


def join_data(
    df_game_box: pd.DataFrame, df_game_summary: pd.DataFrame, df_team: pd.DataFrame
) -> Tuple[pd.DataFrame, pd.DataFrame]:
    if "NameShort" not in df_game_box.columns:
        df_game_box = df_game_box.merge(
            df_team.loc[:, ["TeamId", "NameShort", "Division"]],
            how="inner",
            on="TeamId",
        )
        df_game_box["Player_Team"] = [
            f"{p}_{t}" for p, t in zip(df_game_box["Player"], df_game_box["NameShort"])
        ]
    if "NameShort" not in df_game_summary.columns:
        df_game_summary = df_game_summary.merge(
            df_team.loc[:, ["TeamId", "NameShort", "Division"]],
            how="inner",
            on="TeamId",
        )
        df_game_summary = df_game_summary.sort_values(
            ["ScheduleKey", "TeamId"]
        ).reset_index()
    return (df_game_box, df_game_summary)
