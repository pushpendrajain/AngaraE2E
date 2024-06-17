import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from page_objects.base_page import BasePage


class CheckoutPage(BasePage):
    __email_field = (By.NAME, 'email')
    __first_name = (By.NAME, 'firstName')
    __last_name = (By.NAME, 'lastName')
    __address1 = (By.NAME, 'address1')
    __address1_option = (By.XPATH, "//ul[@id='shipping-address1-options']/li[1]")
    __address2 = (By.NAME, 'address2')
    __city = (By.NAME, 'city')
    __postal_code = (By.NAME, 'postalCode')
    __phone = (By.NAME, 'phone')
    __shipping_btn = (
    By.XPATH, "//button[@class='QT4by _1fragempw rqC98 _1m2hr9gd _1m2hr9ga _7QHNJ VDIfJ j6D1f janiy']")
    __item_label = (
        By.XPATH, "//div[@class='_1fragem2i _1fragemo1 iZ894']/p[@class='_1x52f9s1 _1fragemo1 _1x52f9sv _1fragemqc']")
    __item_desc = (By.XPATH,
                   "//div[@class='_1ip0g651 _1fragemo1 _1fragem5z _1fragem8c _1fragem3c']/p[@class='_1x52f9s1 _1fragemo1 _1x52f9st _1fragemqb _1x52f9sp']")
    __sub_total = (By.XPATH, "//span[@class='_19gi7yt0 _19gi7yts _1fragemqc _19gi7yt2 notranslate']")
    __shipping = (By.XPATH, "//span[@class='_19gi7yt0 _19gi7yts _1fragemqc _19gi7ytj _19gi7yt2 notranslate']")
    __total = (By.XPATH, "//strong[@class='_19gi7yt0 _19gi7yty _1fragemqf _19gi7yt2 notranslate']")
    __quantity = (By.XPATH, "//div[@class='_1m6j2n3e _1fragemnr _1fragemt1 _1fragemtk']/div/div")
    __tax = (By.XPATH, "//div[@class='go06b0']/span")
    __current_area = (By.XPATH, "//li/div[@aria-current='step']")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def set_customer_details(self, email: str, f_name: str, l_name: str, address1: str, address2: str, postal_code: str,
                             phone: str):
        super()._type(self.__email_field, email)
        super()._type(self.__first_name, f_name)
        super()._type(self.__last_name, l_name)
        super()._type(self.__address1, address1)
        super()._click(self.__address1_option)
        time.sleep(3)
        super()._type(self.__address2, address2)
        super()._type(self.__phone, phone)
        super()._type(self.__postal_code, postal_code)
        time.sleep(1)
        super()._take_screenshot("Checkout page after entering customer details")

    def validate_item(self, item: str, stone: str, carat: str, metal: str, qty: str):
        assert super()._get_text(self.__item_label) == item
        print(f'Item validation successful')
        itemdesc = super()._get_text(self.__item_desc)
        if stone in itemdesc:
            print(f'Stone validation successful')
        else:
            print(f'Stone validation failed')
        if carat in itemdesc:
            print(f'Carat validation successful')
        else:
            print(f'Carat validation failed')
        if metal in itemdesc:
            print(f'Metal validation successful')
        else:
            print(f'Metal validation failed')
        assert super()._get_text(self.__quantity) == qty
        print(f'Quantity validation successful')
        super()._take_screenshot("Checkout page")

    def get_subtotal(self) -> str:
        sub_total = super()._get_text(self.__sub_total)
        sub_total = sub_total.replace(',', '')
        sub_total = sub_total.replace('₹', '')
        return sub_total

    def get_shipping(self) -> str:
        return "0"

    def get_total(self) -> str:
        total = super()._get_text(self.__total)
        total = total.replace(',', '')
        total = total.replace('₹', '')
        return total

    def get_tax(self) -> str:
        return super()._get_text(self.__tax)

    def press_continue_btn(self):
        super()._click(self.__shipping_btn)

    def get_current_page(self) -> str:
        page = super()._get_text(self.__current_area)
        super()._take_screenshot(page)
        return page
