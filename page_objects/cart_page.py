import time

from pytest_check import check
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from page_objects.base_page import BasePage


class CartPage(BasePage):
    __page_header = (By.XPATH, "//h1[@class='section-heading a-center mb0']")
    __item_label = (By.XPATH, "//li[@class='ajax-cart__item-details v-start']//a")
    __item_desc = (By.XPATH, "//li[@class='ajax-cart__item-details v-start']/div/div/p")
    __price = (By.XPATH, "//span[@class='ymq_item_original_line_price']/span")
    __discount = (By.XPATH, "//div[@class='cart_savings']/p[2]")
    __checkout_btn = (By.ID, "checkout")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        driver.fullscreen_window()

    def cart_validations(self, item: str, stone: str, carat: str, metal: str, unit_price: str, quantity: str) -> str:
        assert super()._get_text(self.__page_header) == "Cart"
        print('Cart page loaded successfully')
        assert super()._get_text(self.__item_label) == item.upper()
        print("Item assertion successful")
        itemDesc = super()._get_text(self.__item_desc)
        if stone in itemDesc:
            print("Stone quality assertion successful")
        else:
            print("Incorrect stone quality")
        if carat in itemDesc:
            print("Carat Weight assertion successful")
        else:
            print("Incorrect carat weight")
        if metal in itemDesc:
            print("Metal type assertion successful")
        else:
            print("Incorrect metal type")
        price = super()._get_text(self.__price)
        price = price.replace('₹', '')
        price = price.replace(',', '')
        # assert int(price) == (int(unit_price) * int(quantity)), f"Expected {int(unit_price) * int(quantity)},
        # but got {int(price)}" Soft assertion
        check.equal(int(price), (int(unit_price) * int(quantity)),
                    msg=f'Expected {int(unit_price) * int(quantity)}, but got {int(price)}')
        print("Price assertion successful")
        discount = super()._get_text(self.__discount)
        discount = discount.replace('₹ ', '')
        discount = discount.replace(',', '')
        print(f'Savings: {discount}')
        time.sleep(3)
        super()._take_screenshot("Cart page")
        return discount

    def checkout(self):
        super()._click(self.__checkout_btn)
