from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver import Chrome, ChromeOptions
from pathlib import Path
from config import get_chrome_options
from logger import log_info


class GoogleImageSearch:
    def __init__(self, driver: WebDriver):
        pass

    def get_image_links(self, image_name: str):
        pass


class GoogleImage:
    def __init__(self, driver_path: Path):
        self.driver_path = driver_path

    def search(self, image_name: str):
        pass

    def get_image_links(self, image_name: str):
        pass

    def check(self) -> None:
        with Chrome(
            str(self.driver_path), chrome_options=get_chrome_options()
        ) as driver:
            driver.get("https://www.google.com/")
            assert driver.title == "Google"
            log_info(f"All good with driver {driver.title} ...")
