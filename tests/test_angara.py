import time

import pytest

from page_objects.cart_page import CartPage
from page_objects.checkout_page import CheckoutPage
from page_objects.item_page import ItemPage
from page_objects.landing_page import LandingPage


class TestAngara:

    @pytest.mark.e2e
    @pytest.mark.parametrize("item, stoneQuality, cartWeight, metalType, quantity", [
        ("Bezel-Set Round Amethyst Solitaire Pendant", "AAA - Amethyst", "0.8 CT", "14 KT Rose Gold", "3"),
        ("Diamond and Aquamarine Double Circle Pendant Necklace", "AA- Aquamarine", "1.43 CT", "14 KT Yellow Gold", "2")])
    def test_e2e(self, driver, item, stoneQuality, cartWeight, metalType, quantity):
        # Customer address
        email = "Test@gmail.com"
        f_name = "Test"
        l_name = "Test"
        address1 = "Tonk Road Vasundhara Colony Tonk Phatak"
        address2 = "Angara"
        postal_code = "302018"
        phone = "7891370260"

        # Landing page - open URL
        landing_page = LandingPage(driver)
        landing_page.open()
        driver.fullscreen_window()
        landing_page.close_modal()

        # Search Item
        landing_page.search_item(item)
        item_page = ItemPage(driver)
        driver.fullscreen_window()

        # Item page - Select modifications
        assert item_page.get_item_desc() == item
        item_page.select_stone_quality(stoneQuality)
        item_page.select_carat_weight(cartWeight)
        item_page.select_metal_type(metalType)
        item_page.select_quantity(quantity)
        unit_price = item_page.get_unit_price()
        item_page.add_to_cart()

        # Cart page - Validate the cart and selected modifications and checkout
        cart_page = CartPage(driver)
        cart_page.cart_validations(item, stoneQuality, cartWeight, metalType, unit_price, quantity)
        cart_page.checkout()

        # Checkout page/Information page - Enter customer details and validate item selected
        checkout_page = CheckoutPage(driver)
        print("Current page: " + checkout_page.get_current_page())
        driver.fullscreen_window()
        checkout_page.validate_item(item, stoneQuality, cartWeight, metalType, quantity)
        subtotal = checkout_page.get_subtotal()
        shipping = checkout_page.get_shipping()
        total = checkout_page.get_total()
        tax = checkout_page.get_tax()
        print(f'{tax}')
        assert float(total) == (float(shipping)+float(subtotal))
        print("Total is validated")
        checkout_page.set_customer_details(email, f_name, l_name, address1, address2, postal_code, phone)
        checkout_page.press_continue_btn()
        time.sleep(3)

        # Shipping page
        print("Current page: " + checkout_page.get_current_page())
        checkout_page.press_continue_btn()
        time.sleep(2)

        # Payment option selection page
        print("Current page: " + checkout_page.get_current_page())
        # checkout_page.press_continue_btn()


