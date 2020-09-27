import argparse

from src.const import NAME_URL_DICT
from src.crawler import Crawler
from src.preprocess import Preprocesssor
from src.train import Trainer


def run_crawler():
    is_headless = args.headless
    for name in NAME_URL_DICT.keys():
        print(f"==={name}===")
        Crawler(name, is_headless).run()


def run_preprocess():
    Preprocesssor().run()


def run_train():
    Trainer().run()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()
    parser_crawler = subparsers.add_parser("crawler", help="see `crawler -h`")
    parser_crawler.add_argument("--headless", action="store_true", help="headless mode")
    parser_crawler.set_defaults(func=run_crawler)
    parser_preprocess = subparsers.add_parser("preprocess", help="see `preprocess -h`")
    parser_preprocess.set_defaults(func=run_preprocess)
    parser_train = subparsers.add_parser("train", help="see `train -h`")
    parser_train.set_defaults(func=run_train)
    args = parser.parse_args()
    args.func()
