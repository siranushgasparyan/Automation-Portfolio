"""Selenium package"""
from selenium.webdriver.common.by import By
from Helpers.helpers import GeneralHelpers
from testdata import test_data
from selenium.common.exceptions import NoSuchElementException, TimeoutException

class CheckoutPage(GeneralHelpers):
    #locators
    name_input = (By.XPATH, '//input[@id="first-name"]')
    lastname_input = (By.XPATH, '//input[@id="last-name"]')
    postal_code = (By.XPATH, '//input[@id="postal-code"]')
    continue_btn = (By.XPATH, '//input[@id="continue"]')
    cancel_btn = (By.XPATH, '//button[@id="cancel"]')
    error_message = (By.XPATH, '//h3[contains(text(), "Error: First Name is required")]')
    close_btn = (By.XPATH, '//button[@class="error-button"]//*[local-name()="svg"]')

    def fill_checkout_form(self):
        """
        Function to fill all the neccessary fields of checkout form
        """
        try:
            self.find_and_send_keys(self.name_input, test_data.first_name)
            self.find_and_send_keys(self.lastname_input, test_data.last_name)
            self.find_and_send_keys(self.postal_code, test_data.zip_code)
            self.find_and_click(self.continue_btn)
        except Exception as e:
            print(f"Failed to fill the checkout input: {e}")
    
    def leave_form_empty(self):
        """
        Function to click the Continue button without filling the form
        """
        try:
            self.find_and_click(self.continue_btn)
        except Exception as e:
            print(f"Failed to find the Continue button: {e}")

    def close_the_error(self):
        """
        Function to click the Close button of the error message
        """
        try:
            self.find_and_click(self.close_btn)
        except Exception as e:
            print(f"Failed to find the Continue button: {e}")