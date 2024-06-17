import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from page_objects.base_page import BasePage


class LandingPage(BasePage):
    __url = "https://www.angara.in/"
    __modal_close = (By.XPATH, "//div[@class='ecomsend__Modal__CloseButton _closeBtn_4tu8s_236']")
    __search_btn = (By.XPATH, "//a[@data-wau-slideout-target='searchbox']")
    __search_field = (By.ID, "q")
    __search_field1 = (By.ID, "gl-d-searchbox-input")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        super()._open_url(self.__url)
        super()._take_screenshot("Landing page")

    def close_modal(self):
        try:
            super()._click(self.__modal_close)
        except NoSuchElementException:
            pass

    def search_item(self, item: str):
        locator = (By.LINK_TEXT, item)
        super()._click(self.__search_btn)
        super()._click(self.__search_field)
        super()._type(self.__search_field1,item)
        # time.sleep(3)
        super()._click(locator)
