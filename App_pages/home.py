from selenium.webdriver.common.by import By
from Helpers.helpers import GeneralHelpers
from selenium.common.exceptions import NoSuchElementException, TimeoutException

class HomePage(GeneralHelpers):
    #locators
    add_to_cart_btn1 = (By.XPATH, '//button[@id="add-to-cart-sauce-labs-backpack"]')
    add_to_cart_btn2 = (By.XPATH, '//button[@id="add-to-cart-sauce-labs-bike-light"]')
    shopping_cart_link = (By.XPATH, "//a[@class='shopping_cart_link']")
    shopping_cart_badge = (By.XPATH, "//span[@class='shopping_cart_badge']")
    items_list = []
    items_title_list_home = (By.XPATH, "//div[@class='inventory_item_name']")

    def add_to_cart(self):
        """
        Function to add products to the cart,
        add update the cart_list _length every time when adding a new product
        """
        try:
            self.find_and_click(self.add_to_cart_btn1)
            self.find_and_click(self.add_to_cart_btn2)
        except Exception as e:
            print(f"Failed to add items to cart: {e}")

        if self.find(self.shopping_cart_badge):
            print("Added to cart!")
        
        self.find_and_click(self.shopping_cart_link)