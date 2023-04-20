"""Import neccessary modules"""
import pytest
from Helpers.helpers import GeneralHelpers
from App_pages.home import HomePage
from App_pages.login import LogIn
from testdata import test_data
from selenium.webdriver.support import expected_conditions as EC
from App_pages.your_card import *
from selenium import webdriver
import allure

@pytest.mark.order(7)
def test_add_to_card(driver):
    """
    Test to check products count after removing one of them
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

    badge = HomePage.shopping_cart_badge
    #Check if shopping card bage is visible
    assert badge is not None, "Shopping cart badge not found"

    shopping_cart_badge_xpath = your_card_page.shopping_cart_badge
    badge_txt = driver.find_element(*shopping_cart_badge_xpath).text

    #Check if the shopping cart badge number is 2, after adding 2 items
    # which should correspond to the number of items added to the cart
    assert badge_txt == '2', "Wrong bage number"

    your_card_page.click_remove_button()

    badge_new_txt = driver.find_element(*shopping_cart_badge_xpath).text

    #Check if the shopping cart badge number is 1, after removing one item
    # which should correspond to the number of items added to the cart
    assert badge_new_txt == '1', "Wrong bage number"