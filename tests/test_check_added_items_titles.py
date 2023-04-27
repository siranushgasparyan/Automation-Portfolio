"""Import neccessary modules"""
import pytest
from Helpers.helpers import GeneralHelpers
from App_pages.home import HomePage
from App_pages.login import LogIn
from testdata import test_data
from App_pages.your_card import *
from selenium import webdriver
import allure

@pytest.mark.order(8)
def test_add_to_card(driver):
    """
    Test case to check if added items titles are correct in the Your Cart page
    """
    login_page_url = test_data.login_url
    helper = GeneralHelpers(driver)
    helper.go_to_page(login_page_url)

    login_page = LogIn(driver)
    login_page.login()

    home_page = HomePage(driver)
    home_page.add_to_cart()

    titles_list = home_page.items_title_list_home
    titles_txt_list = driver.find_elements(*titles_list)

    first_item_title = titles_txt_list[0].text
    second_item_title = titles_txt_list[1].text

    your_card_page = YourCart(driver)
    titles_list2 = your_card_page.items_title_list_cart
    titles_txt_list2 = driver.find_elements(*titles_list2)

    first_item_title2 = titles_txt_list2[0].text
    second_item_title2 = titles_txt_list2[1].text   

    #Check if the added items titles are the same in the Home and Your cart pages
    assert first_item_title == first_item_title2, "Wrong first item title"
    assert second_item_title == second_item_title2, "Wrong second item title"