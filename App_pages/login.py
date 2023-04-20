"""Selenium package"""
from selenium.webdriver.common.by import By
from Helpers.helpers import GeneralHelpers
from creddentials import creds
from selenium.common.exceptions import NoSuchElementException, TimeoutException

class LogIn(GeneralHelpers):
    #locators
    username_input = (By.XPATH, "//input[@id ='user-name']")
    passwrod_input = (By.XPATH, "//input[@id ='password']")
    login_button = (By.XPATH, "//input[@id ='login-button']")
    email = creds['email']
    password = creds['password']
    
    def login(self):
        """Login function"""
        try:
            self.find_and_send_keys(self.username_input, self.email)
            self.find_and_send_keys(self.passwrod_input, self.password)
            self.find_and_click(self.login_button)
        except Exception as e:
            print(f"Failed to login {e}")

    def empty_login(self):
        """
        Function for clicking the "Login" button without filling out the login form
        """
        try:
            self.find_and_click(self.login_button)
        except Exception as e:
            print(f"Failed to login {e}")