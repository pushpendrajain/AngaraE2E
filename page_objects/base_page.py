import time
from datetime import datetime

import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:
    def __init__(self, driver: WebDriver):
        self._driver = driver

    def _open_url(self, url: str):
        self._driver.get(url)

    def _find(self, locator: tuple) -> WebElement:
        return self._driver.find_element(*locator)

    def _finds(self, locator: tuple, time: int = 10) -> list[WebElement]:
        self._wait_until_element_is_visible(locator, time)
        return self._driver.find_elements(*locator)

    def _type(self, locator: tuple, text: str, time: int = 10):
        self._wait_until_element_is_visible(locator, time)
        self._find(locator).send_keys(text)

    def _click(self, locator: tuple, time: int = 10):
        self._wait_until_element_is_visible(locator, time)
        self._find(locator).click()

    def _get_text(self, locator: tuple, time: int = 10) -> str:
        self._wait_until_element_is_visible(locator, time)
        return self._find(locator).text

    def _wait_until_element_is_visible(self, locator: tuple[str, str], time: int = 10):
        wait = WebDriverWait(self._driver, time)
        wait.until(ec.visibility_of_element_located(locator))

    def _take_screenshot(self, name: str):
        time.sleep(1)
        curr_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S').replace('-', '_').replace(':', '_').replace(' ', "")
        file_name = name + curr_time + ".png"
        self._driver.save_screenshot("reports/screenshots/"+file_name)







