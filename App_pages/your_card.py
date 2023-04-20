"""Selenium package"""
from selenium.webdriver.common.by import By
from Helpers.helpers import GeneralHelpers
from selenium.common.exceptions import NoSuchElementException, TimeoutException

class YourCart(GeneralHelpers):
    #locators
    checkout_btn = (By.XPATH, '//button[@id="checkout"]')
    continue_shopping_btn = (By.XPATH, '//button[@id="continue-shopping"]')
    item_price = (By.XPATH, '//div[@class="inventory_item_price"]')
    remove_btn = (By.XPATH, '//button[@id="remove-sauce-labs-bike-light"]')
    shopping_cart_badge = (By.XPATH, '//span[@class="shopping_cart_badge"]')
    items_title_list_cart = (By.XPATH, "//div[@class='inventory_item_name']")

    def click_checkout(self):
        """Fuction to click the chekout button"""
        try:
            self.find_and_click(self.checkout_btn)
        except Exception as e:
            print(f"Failed to find and/or click the Checkout button ")

    def click_continue_shopping(self):
        """Function to click the Continue Shopping button"""
        try:
            self.find_and_click(self.continue_shopping_btn)
        except Exception as e:
            print(f"Failed to find and/or click the Continue button ")

    def check_price(self):
        """
        Function to check if the sum of the added products price is currect
        """
        elements = self.find_all(self.item_price)
        price_list = []
        for el in elements:
            price_list.append(el.text)
        price_list_number = []
        for el in price_list:
            global price
            price = float(el.split('$')[1])
            price_list_number.append(price)
        return price_list_number
    
    def click_remove_button(self):
        """
        Function to click the Remove button
        """
        try:
            self.find_and_click(self.remove_btn)
        except Exception as e:
            print(f"Failed to click the Remove button")