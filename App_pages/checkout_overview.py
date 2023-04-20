"""Selenium package"""
from selenium.webdriver.common.by import By
from Helpers.helpers import GeneralHelpers
from selenium.common.exceptions import NoSuchElementException, TimeoutException

class CheckoutOverviewPage(GeneralHelpers):
    #locators
    prices_xpath = (By.XPATH, '//div[@class="inventory_item_price"]')
    tax = (By.XPATH, '//div[@class="summary_tax_label"]')
    total = (By.XPATH, '//div[@class="summary_info_label summary_total_label"]')
    finish_btn = (By.XPATH, '//button[@id="finish"]')

    def find_price_num(self):
        """
        Function to find products price
        """
        prices = self.find_all(self.prices_xpath)
        price_list = []
        for el in prices:
            price_list.append(el.text)
        price_list_number = []   
        for el in price_list:
            global price2
            price2 = float(el.split('$')[1])
            price_list_number.append(price2)
        return price_list_number
    
    def click_finish_button(self):
        """
        Function to click the Finish button
        """
        try:
            self.find_and_click(self.finish_btn)
        except Exception as e:
            print(f"Failed to find the Finis button: {e}")