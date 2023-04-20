"""Selenium package"""
from selenium.webdriver.common.by import By
from Helpers.helpers import GeneralHelpers
from selenium.common.exceptions import NoSuchElementException, TimeoutException

class CheckoutCmpletePage(GeneralHelpers):
    #locators
    complete_header = (By.XPATH, "//h2[@class='complete-header']")
    page_title = (By.XPATH, "//span[@class='title']")
    back_home_btn = (By.XPATH, "//button[@id='back-to-products']")

    def click_back_button(self):
        """
        Fnction to click Back Home button
        """
        try:
            self.find_and_click(self.back_home_btn)
        except Exception as e:
            print(f"Failed to click the Back Home button: {e}")