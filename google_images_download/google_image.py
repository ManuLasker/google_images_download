from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from config import ImgTagHasSrc
from validators import ImageSrcBase64, ImageSrcUrl

from typing import List, Tuple
from pathlib import Path
from config import get_chrome_options
from logger import log_info

import time


class GoogleImage:
    def __init__(self, driver: WebDriver, max_scroll: int):
        search_image_button: WebElement = driver.find_element_by_class_name(
            "hide-focus-ring"
        )
        search_image_button.click()
        self.driver = driver
        self.xpath = "//img[@class='rg_i Q4LuWd']"
        self.scroll_to_element = "arguments[0].scrollIntoView(true);"
        self.max_scroll = max_scroll

    def get_image_links(self) -> Tuple[List[ImageSrcUrl], List[ImageSrcBase64]]:
        img_results: List[WebElement] = self.driver.find_elements_by_xpath(self.xpath)
        # Create urls, base64  for image searched
        image_urls, images_base64 = [], []
        # loop through images results
        index, max_scroll = 0, self.max_scroll
        while index < len(img_results) and max_scroll != 0:
            try:
                img_src: str = WebDriverWait(img_results[index], 10).until(
                    ImgTagHasSrc()
                )
                try:
                    temp = ImageSrcUrl(url=img_src)
                    if not temp in image_urls:
                        image_urls.append(temp)
                except:
                    temp = ImageSrcBase64(base64_src=img_src)
                    if not temp in images_base64:
                        images_base64.append(temp)
            except Exception as error:
                log_info(f"There was an error getting image source {error}")
            index += 1
            if index == len(img_results):
                self.driver.execute_script(
                    self.scroll_to_element, img_results[index - 1]
                )
                time.sleep(1.5)  # wait till it scroll down complete
                img_results: List[WebElement] = self.driver.find_elements_by_xpath(
                    self.xpath
                )[index:]
                index = 0
                max_scroll -= 1
                log_info(
                    f"Doing a scroll down, Images scrapped:"
                    f" = {len(image_urls) + len(images_base64)}"
                )
        return image_urls, images_base64


class Google:
    def __init__(self, driver_path: Path):
        self.driver_path = driver_path
        self.url = "https://www.google.com/search?q={}"

    def search(
        self, query_search: str, max_scroll: int = 3
    ) -> Tuple[List[ImageSrcUrl], List[ImageSrcBase64]]:
        with Chrome(self.driver_path) as driver:
            # search in google
            driver.get(self.url.format(query_search))
            # wait
            time.sleep(0.5)
            # search in image section
            google_image = GoogleImage(driver, max_scroll)
            return google_image.get_image_links()

    def check(self) -> None:
        with Chrome(self.driver_path, chrome_options=get_chrome_options()) as driver:
            driver.get("https://www.google.com/")
            assert driver.title == "Google"
            log_info(f"All good with driver {driver.title} ...")
