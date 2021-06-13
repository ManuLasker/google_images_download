from selenium.webdriver import ChromeOptions
from logger import log_info
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.chrome.webdriver import WebDriver
from typing import Union, List


def get_chrome_options(check: bool = True) -> ChromeOptions:
    chrome_options = ChromeOptions()
    chrome_options.headless = True
    return chrome_options


class ImgTagHasSrc:
    def __call__(self, img_result: WebElement) -> Union[str, bool]:
        src: str = img_result.get_attribute("src")
        if src:
            return src
        else:
            data_src: str = img_result.get_attribute("data-src")
            return data_src if data_src else False
