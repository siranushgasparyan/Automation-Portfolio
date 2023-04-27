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
import allure

@pytest.mark.order(5)
def test_add_to_card(driver):
    """
    Test case to check the final total price of the products
    """
    global price2
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
    checkout_second_page.find_price_num()

    price2 = checkout_second_page.find_price_num()
    checkout_second_page.find_price_num()
    price_one = price2[0]
    price_two = price2[1]

    total_xpath = checkout_second_page.total
    total_txt = driver.find_element(*total_xpath).text  
    total_clean = float(total_txt.split("Total: $")[1])

    tax_xpath = checkout_second_page.tax
    tax_txt = driver.find_element(*tax_xpath).text 
    tax_clean = float(tax_txt.split("Tax: $")[1])
    
    #Check if total price of the added products is correct
    assert price_one + price_two + tax_clean == total_clean, "Incorrect total price"