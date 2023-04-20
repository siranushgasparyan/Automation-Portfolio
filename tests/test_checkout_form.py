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
import allure

@pytest.mark.order(3)
def test_add_to_card(driver):
    """
    Test case for adding products to card
    """
    login_page_url = test_data.login_url
    helper = GeneralHelpers(driver)
    helper.go_to_page(login_page_url)

    login_page = LogIn(driver)
    login_page.login()

    home_page = HomePage(driver)
    home_page.add_to_cart()

    your_card_page = YourCart(driver)
    your_card_page.click_checkout()

    # Check if the URL contains "checkout-step-one"
    WebDriverWait(driver, 10).until(EC.url_contains("checkout-step-one"))
    assert "checkout-step-one" in driver.current_url, "Failed to open checkout step two page"

    checkot_first_page = CheckoutPage(driver)
    checkot_first_page.fill_checkout_form()

    # Check if the URL contains "checkout-step-two"
    WebDriverWait(driver, 10).until(EC.url_contains("checkout-step-two"))
    assert "checkout-step-two" in driver.current_url, "Failed to open checkout step two page"