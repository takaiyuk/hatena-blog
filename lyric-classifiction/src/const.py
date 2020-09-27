from dataclasses import dataclass

PATH = {
    "driver": {"default": "/usr/bin/chromedriver", "local": "./drivers/chromedriver"},
}

TOP_URL = "http://j-lyric.net/"
NAME_URL_DICT = {
    "AL": "http://j-lyric.net/artist/a05b368/",
    "andymori": "http://j-lyric.net/artist/a050bf1/",
    "長澤知之": "http://j-lyric.net/artist/a04e0c2/",
}


@dataclass
class Prefix:
    interim: str = "./data/interim"
    processed: str = "./data/processed"
    raw: str = "./data/raw"


@dataclass
class RawPath:
    al: str = f"{Prefix.raw}/AL.jbl"
    andymori: str = f"{Prefix.raw}/andymori.jbl"
    nagasawa: str = f"{Prefix.raw}/長澤知之.jbl"


@dataclass
class InterimPath:
    al: str = f"{Prefix.interim}/al.jbl"
    andymori: str = f"{Prefix.interim}/andymori.jbl"
    nagasawa: str = f"{Prefix.interim}/nagasawa.jbl"


@dataclass
class ProcessedPath:
    al: str = f"{Prefix.processed}/al.jbl"
    andymori: str = f"{Prefix.processed}/andymori.jbl"
    nagasawa: str = f"{Prefix.processed}/nagasawa.jbl"


@dataclass
class DataPath:
    interim: InterimPath = InterimPath
    processed: ProcessedPath = ProcessedPath
    raw: RawPath = RawPath
