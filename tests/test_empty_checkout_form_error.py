"""Import neccessary modules"""
from Helpers.helpers import GeneralHelpers
from App_pages.home import HomePage
from App_pages.login import LogIn
from testdata import test_data
import pytest
from App_pages.checkout_your_info import CheckoutPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from App_pages.your_card import YourCart
from selenium import webdriver
import allure

@pytest.mark.order(4)
def test_add_to_card(driver):
    """
    Test case for adding products to card
    """
    driver = webdriver.Chrome()
    login_page_url = test_data.login_url
    helper = GeneralHelpers(driver)
    helper.go_to_page(login_page_url)

    login_page = LogIn(driver)
    login_page.login()

    home_page = HomePage(driver)
    home_page.add_to_cart()

    your_card_page = YourCart(driver)
    your_card_page.click_checkout()

    # Check if the URL contains "checkout-step-one" keyword
    WebDriverWait(driver, 10).until(EC.url_contains("checkout-step-one"))
    assert "checkout-step-one" in driver.current_url, "Failed to open checkout step two page"

    checkot_first_page = CheckoutPage(driver)
    checkot_first_page.leave_form_empty()

    error_message = test_data.checkout_page1_error
    error_msg_xpath = CheckoutPage.error_message
    error_txt = driver.find_element(*error_msg_xpath).text

    #Check if error message is: "Error: First Name is required"
    assert error_txt == error_message, "Wrong error message"
