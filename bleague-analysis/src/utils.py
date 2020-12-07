import pandas as pd


class FourFactors:
    @staticmethod
    def TOV(TOV: int, FGA: int, FTA: int) -> float:
        """
        TOV% = TOV / (FGA + FTA x 0.44 + TOV)
        """
        return TOV / (FGA + FTA * 0.44 + TOV)

    @staticmethod
    def eFG(FG2M: int, FG3M: int, FGA: int) -> float:
        """
        eFG% = (FG + 0.5 x 3P) / FGA
        """
        return (FG2M + 0.5 * FG3M) / FGA

    @staticmethod
    def ORB(ORB: int, OppDRB: int) -> float:
        """
        OREB% = ORB / (ORB + OppDRB)
        """
        return ORB / (ORB + OppDRB)

    @staticmethod
    def FT(FTA: int, FGA: int) -> float:
        """
        FTR = FTA / FGA
        """
        return FTA / FGA


def calc_posession(FGA: int, TO: int, FTA: int, OR: int) -> float:
    """
        ref. https://www.nbastuffer.com/analytics101/possession/
        - FGA: Field Goal Attempts
        - TO: Turnovers
        - FTA: Free Throw Attempts
        - OR: Offensive Rebounds
        """
    return 0.96 * (FGA + TO + 0.44 * FTA - OR)


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


def get_possession(df_game_summary: pd.DataFrame) -> pd.DataFrame:
    df_game_summary["Posession"] = [
        calc_posession(F2GA + F3GA, TO, FTA, OR)
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
    df_game_summary = get_possession(df_game_summary)
    for k in ["PTS", "Posession", "OR", "DR", "TO"]:
        df_game_summary = get_opponent(df_game_summary, k)
    for num, denom in zip(
        ["TO", "TO_opponent", "PTS", "PTS_opponent"],
        ["Posession", "Posession_opponent", "Posession", "Posession_opponent"],
    ):
        df_game_summary[f"{num}_per_{denom}"] = (
            100 * df_game_summary[num] / df_game_summary[denom]
        )
    return df_game_summary
