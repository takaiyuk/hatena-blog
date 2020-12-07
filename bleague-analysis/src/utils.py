from typing import Tuple

import pandas as pd


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


def get_opponent(df_game_summary: pd.DataFrame, key_col: str) -> pd.DataFrame:
    key_opponent = {
        k: df_group[key_col].values.tolist()
        for k, df_group in df_game_summary.loc[:, ["ScheduleKey", key_col]].groupby(
            "ScheduleKey"
        )
    }
    df_game_summary[f"{key_col}_opponent"] = df_game_summary["ScheduleKey"].apply(
        lambda x: key_opponent.get(x)
    )
    df_game_summary[f"{key_col}_opponent"] = [
        key_list[0] if i % 2 else key_list[1]
        for i, key_list in enumerate(df_game_summary[f"{key_col}_opponent"])
    ]
    return df_game_summary


def calc_possession(df_game_summary: pd.DataFrame) -> pd.DataFrame:
    def _calc_posession(FGA: int, TO: int, FTA: int, OR: int) -> float:
        """
        ref. https://www.nbastuffer.com/analytics101/possession/
        - FGA: Field Goal Attempts
        - TO: Turnovers
        - FTA: Free Throw Attempts
        - OR: Offensive Rebounds
        """
        return 0.96 * (FGA + TO + 0.44 * FTA - OR)

    df_game_summary["Posession"] = [
        _calc_posession(F2GA + F3GA, TO, FTA, OR)
        for F2GA, F3GA, TO, FTA, OR in zip(
            df_game_summary["F2GA"],
            df_game_summary["F3GA"],
            df_game_summary["TO"],
            df_game_summary["FTA"],
            df_game_summary["OR"],
        )
    ]
    return df_game_summary


def preprocess_game_summary(df_game_summary: pd.DataFrame) -> pd.DataFrame:
    df_game_summary = calc_possession(df_game_summary)
    for k in ["PTS", "Posession"]:
        df_game_summary = get_opponent(df_game_summary, k)
    df_game_summary["TO_per_Posession"] = (
        100 * df_game_summary["TO"] / df_game_summary["Posession"]
    )
    df_game_summary["PTS_per_Posession"] = (
        100 * df_game_summary["PTS"] / df_game_summary["Posession"]
    )
    df_game_summary["PTS_opponent_per_Posession"] = (
        100 * df_game_summary["PTS_opponent"] / df_game_summary["Posession_opponent"]
    )
    return df_game_summary
