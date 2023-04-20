"""Import neccessary modules"""
import pytest
from Helpers.helpers import GeneralHelpers
from App_pages.home import HomePage
from App_pages.login import LogIn
from testdata import test_data
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from App_pages.your_card import *
import allure

@pytest.mark.order(2)
def test_add_to_card(driver):
    """
    Test case for adding products to card
    """
    global price
    login_page_url = test_data.login_url
    helper = GeneralHelpers(driver)
    helper.go_to_page(login_page_url)

    login_page = LogIn(driver)
    login_page.login()

    home_page = HomePage(driver)
    home_page.add_to_cart()

    your_card_page = YourCart(driver)
    price = your_card_page.check_price()
    your_card_page.check_price()

    #Check if the products price total is currect
    price1 = price[0]
    price2 = price[1]
    assert price1 + price2 == 39.98, 'Result is incorrect'

    #Check if the shopping cart bage is visible
    badge = HomePage.shopping_cart_badge
    assert badge is not None, "Shopping cart badge not found"

    #Check if page URL contains "cart" keyword
    WebDriverWait(driver, 10).until(EC.url_contains("cart"))
    assert "cart" in driver.current_url, "Failed to open cart"