from selenium.webdriver import ChromeOptions


def get_chrome_options(check: bool = True) -> ChromeOptions:
    chrome_options = ChromeOptions()
    chrome_options.headless = True
    return chrome_options
