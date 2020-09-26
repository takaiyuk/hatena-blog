import os
import random
import time
from abc import ABCMeta
from typing import Any, List

import joblib
import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import Select

from src.const import NAME_URL_DICT, PATH, TOP_URL


class Browser:
    def __init__(self, driver) -> None:
        self.driver = driver

    def _get_random(self, a: float = 0.8, b: float = 1.2) -> None:
        return random.uniform(a, b)

    def _sleep(self, a: float = 0.8, b: float = 1.2) -> None:
        ts = self._get_random(a, b)
        time.sleep(ts)

    def back(self) -> None:
        self.driver.back()
        self._sleep()

    def click(self, xpath: str) -> None:
        self.driver.find_element_by_xpath(xpath).click()
        self._sleep()

    def click_on_class(self, class_):
        self.driver.find_elements_by_class_name(class_).click()
        self._sleep()

    def current_url(self) -> str:
        return self.driver.current_url

    def find_class_element(self, class_: str) -> List[str]:
        class_list = self.driver.find_elements_by_class_name(class_)
        self._sleep()
        return class_list

    def get(self, url: str) -> None:
        self.driver.get(url)
        self._sleep()

    def quit(self):
        self.driver.quit()

    def save(self, filepath: str) -> None:
        html = self.driver.page_source
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(html)

    def scroll(self, height: int) -> None:
        self.driver.execute_script("window.scrollTo(0, " + str(height) + ");")

    def send(self, xpath: str, string: str) -> None:
        self.driver.find_element_by_xpath(xpath).send_keys(string)
        self._sleep()

    def source(self) -> str:
        return self.driver.page_source


class AbstractCrawler(metaclass=ABCMeta):
    def __init__(self, name, is_headless: bool = True) -> None:
        self.name = name

        options = webdriver.ChromeOptions()
        if is_headless:
            options.add_argument("--headless")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-gpu")
            options.add_argument("--window-size=1280x1696")
            options.add_argument("--disable-application-cache")
            options.add_argument("--disable-infobars")
            options.add_argument("--hide-scrollbars")
            options.add_argument("--enable-logging")
            options.add_argument("--log-level=0")
            options.add_argument("--single-process")
            options.add_argument("--ignore-certificate-errors")
            options.add_argument("--disable-dev-shm-usage")
        if os.path.exists(PATH["driver"]["default"]):
            executable_path = PATH["driver"]["default"]
        elif os.path.exists(PATH["driver"]["local"]):
            executable_path = PATH["driver"]["local"]
        else:
            raise Exception("driver path is not found")
        driver = webdriver.Chrome(executable_path=executable_path, options=options)
        self.browser = Browser(driver)


class Crawler(AbstractCrawler):
    def _get_lyric(self, idx: int) -> str:
        xpath = f'//*[@id="ly{idx}"]/p[1]/a'
        title = self.browser.driver.find_element_by_xpath(xpath).text.split("\n")[0]
        print(title)
        self.browser.click(xpath)
        self.browser.scroll(height=10000)
        page_source = self.browser.source()
        self.browser.back()
        self.browser.scroll(height=10000)
        return page_source

    def _save(self, obj: Any, p: str) -> None:
        joblib.dump(obj, p, compress=3)

    def run(self) -> None:
        try:
            # トップページ
            self.browser.get(TOP_URL)

            if self.name == "AL":
                self.browser.get(NAME_URL_DICT[self.name])
            else:
                # 検索でドロップダウンから歌手名を選択
                opsel_element = self.browser.driver.find_element_by_id("opsel")
                Select(opsel_element).select_by_value("2")

                # 検索で歌手名を入力、検索ボタンをクリック
                self.browser.send('//*[@id="keyword"]', self.name)
                self.browser.click('//*[@id="ebox"]/div[2]/form/input[6]')

                # 検索結果から一番上をクリック
                self.browser.click('//*[@id="mnb"]/div[2]/p[1]/a')

            # リスト数を取得
            num_list = 1000
            for i in range(1000):
                i += 1
                try:
                    self.browser.driver.find_element_by_id(f"ly{i}")
                except selenium.common.exceptions.NoSuchElementException:
                    num_list = i - 1
                    print(f"num_list: {num_list}")
                    break

            # 歌詞リストが一覧で表示される：曲名をクリック・歌詞取得・1ページ前に戻るを繰り返す
            page_sources = [""] * num_list
            for i in range(num_list):
                idx = i + 1
                page_source = self._get_lyric(idx)
                page_sources[i] = page_source

            # 保存
            filepath = f"data/raw/{self.name}.jbl"
            self._save(page_sources, filepath)

        finally:
            # プロセス消す
            self.browser.quit()
