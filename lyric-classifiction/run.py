import argparse

from src.const import NAME_URL_DICT
from src.crawler import Crawler

parser = argparse.ArgumentParser()
# parser.add_argument("--start", type=str, required=True, help="start date")
# parser.add_argument("--end", type=str, required=True, help="end date")
parser.add_argument("--headless", action="store_true", help="headless mode")
args = parser.parse_args()
is_headless = args.headless
# start_date = args.start
# end_date = args.end

if __name__ == "__main__":
    for name in NAME_URL_DICT.keys():
        print(f"==={name}===")
        Crawler(name, is_headless).run()
