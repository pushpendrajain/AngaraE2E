from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from page_objects.base_page import BasePage


class ItemPage(BasePage):
    # _url = "https://www.angara.in/products/bezel-set-round-amethyst-solitaire-pendant"
    __item_dec = (By.XPATH, "//div[@class='sticky--content']/h1")
    __stone_quality_list = (By.XPATH, "//div[@option-name='Stone Quality']//ul/li")
    __selected_stone_quality = (By.XPATH, "//div[@option-name='Stone Quality']//legend/label/span[2]")
    __carat_weight_option = (By.XPATH, "//div[@type='select']")
    __carat_weight_hidden_list = (By.XPATH, "//ul[@class='swatch-drop-down-list swatch-hide']")
    __carat_weight_visible_list = (By.XPATH, "//ul[@class='swatch-drop-down-list']")
    __carat_weight_list = (By.XPATH, "//div[@option-name='Carat Weight']//ul/li")
    __selected_carat_weight = (By.XPATH, "//div[@type='select']//span/span")
    __metal_type_list = (By.XPATH, "//div[@option-name='Metal Type']//ul/li")
    __selected_metal_type = (By.XPATH, "//div[@option-name='Metal Type']//legend/label/span[2]")
    __item_field = (By.NAME, 'quantity')
    __unit_price = (By.XPATH, "//span[@class='price-item price-item--regular']")
    __add_to_cart_btn = (By.ID, 'add-to-card-btn')
    __quantity_input_field = (By.NAME, 'quantity')

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def get_item_desc(self) -> str:
        super()._take_screenshot("Item page")
        return super()._get_text(self.__item_dec)

    def select_stone_quality(self, stone_quality: str):
        wait = WebDriverWait(self._driver, 10)
        print("Selecting stone quality: " + stone_quality)
        stone = super()._finds(self.__stone_quality_list)
        for i in stone:
            d = i.get_attribute("orig-value")
            if d == stone_quality:
                i.click()
                break
        stoneQlty = super()._get_text(self.__selected_stone_quality)
        print("Stone quality selected: " + stoneQlty)

    def select_carat_weight(self, carat_weight: str):
        wait = WebDriverWait(self._driver, 10)
        print("Selecting carat weight: " + carat_weight)
        if super()._find(self.__carat_weight_hidden_list):
            super()._click(self.__carat_weight_option)
            if super()._find(self.__carat_weight_visible_list):
                carat = super()._finds(self.__carat_weight_list)
                for i in carat:
                    d = i.get_attribute("orig-value")
                    if d == carat_weight:
                        i.click()
                        break
        carat_wget = super()._get_text(self.__selected_carat_weight)
        print("Carat Weight selected: " + carat_wget)

    def select_metal_type(self, metal_type: str):
        wait = WebDriverWait(self._driver, 10)
        print("Selecting metal type: " + metal_type)
        metal = super()._finds(self.__metal_type_list)
        for i in metal:
            d = i.get_attribute("orig-value")
            if d == metal_type:
                i.click()
                break
        metal_type_selected = super()._get_text(self.__selected_metal_type)
        print("Stone quality selected: " + metal_type_selected)

    def get_unit_price(self) -> str:
        unitPrice = super()._get_text(self.__unit_price, 10)
        unitPrice = unitPrice.replace('₹ ', '')
        unitPrice = unitPrice.replace(',', '')
        print(f'Unit price: {unitPrice}')
        super()._take_screenshot("After selecting choice")
        return unitPrice

    def select_quantity(self, quantity: str = '1'):
        super()._type(self.__quantity_input_field, Keys.BACK_SPACE + Keys.DELETE)
        super()._type(self.__quantity_input_field, quantity)

    def add_to_cart(self):
        super()._click(self.__add_to_cart_btn)
