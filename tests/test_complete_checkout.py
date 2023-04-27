"""Import neccessary modules"""
from Helpers.helpers import GeneralHelpers
from App_pages.home import HomePage
from App_pages.login import LogIn
from testdata import test_data
import pytest
from App_pages.checkout_your_info import CheckoutPage
from App_pages.your_card import YourCart
from App_pages.checkout_overview import CheckoutOverviewPage
from selenium import webdriver
from App_pages.checkout_complete import CheckoutCmpletePage
import allure

@pytest.mark.order(6)
def test_add_to_card(driver):
    """
    Test case to check the checkout completion
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

    checkot_first_page = CheckoutPage(driver)
    checkot_first_page.fill_checkout_form()

    checkout_second_page = CheckoutOverviewPage(driver)
    checkout_second_page.click_finish_button()

    assert "checkout-complete" in driver.current_url, "Failed to checkout"

    checkout_complete_page = CheckoutCmpletePage(driver)

    complete_header_xpath = checkout_complete_page.complete_header
    header_txt = driver.find_element(*complete_header_xpath).text

    #Check if the page header text is "Thank you for your order!"
    assert header_txt == test_data.complete_header_text, "Incorrect Header Text"

    checkout_complete_page.click_back_button()

    # Check if the URL contains "inventory.html"
    assert "inventory.html" in driver.current_url, "Failed to login"
