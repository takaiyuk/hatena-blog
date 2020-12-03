"""
Thanks to https://github.com/rintaromasuda/bleaguer/tree/master/inst/extdata
"""

from dataclasses import dataclass

prefix = "https://raw.githubusercontent.com/rintaromasuda/bleaguer/master/inst/extdata"


@dataclass
class EventData:
    events: str = f"{prefix}/events.csv"


@dataclass
class GameData:
    games_201617: str = f"{prefix}/games_201617.csv"
    games_201718: str = f"{prefix}/games_201718.csv"
    games_201819: str = f"{prefix}/games_201819.csv"
    games_201920: str = f"{prefix}/games_201920.csv"
    games_202021: str = f"{prefix}/games_202021.csv"


@dataclass
class GameBoxScoreData:
    games_boxscore_201617: str = f"{prefix}/games_boxscore_201617.csv"
    games_boxscore_201718: str = f"{prefix}/games_boxscore_201718.csv"
    games_boxscore_201819: str = f"{prefix}/games_boxscore_201819.csv"
    games_boxscore_201920: str = f"{prefix}/games_boxscore_201920.csv"
    games_boxscore_202021: str = f"{prefix}/games_boxscore_202021.csv"


@dataclass
class GameSummaryData:
    games_summary_201617: str = f"{prefix}/games_summary_201617.csv"
    games_summary_201718: str = f"{prefix}/games_summary_201718.csv"
    games_summary_201819: str = f"{prefix}/games_summary_201819.csv"
    games_summary_201920: str = f"{prefix}/games_summary_201920.csv"
    games_summary_202021: str = f"{prefix}/games_summary_202021.csv"


@dataclass
class TeamData:
    teams: str = f"{prefix}/teams.csv"
