import argparse

from src.const import NAME_URL_DICT
from src.crawler import Crawler

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers()
parser_crawler = subparsers.add_parser("crawler", help="see `crawler -h`")
parser_crawler.add_argument("--headless", action="store_true", help="headless mode")
# parser_crawler = subparsers.add_parser("analyze", help="see `analyze -h`")
# parser_crawler.add_argument("--hoge", type=str, required=False, help="hogehoge")

args = parser.parse_args()

if __name__ == "__main__":
    if hasattr(args, "headless"):
        is_headless = args.headless
        for name in NAME_URL_DICT.keys():
            print(f"==={name}===")
            Crawler(name, is_headless).run()
