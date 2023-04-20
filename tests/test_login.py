from Helpers.helpers import GeneralHelpers
from App_pages.login import LogIn
from testdata import test_data
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import allure

@pytest.mark.order(1)
def test_login(driver):
    """
    Test case for login page
    """
    login_page_url = test_data.login_url
    helper = GeneralHelpers(driver)
    helper.go_to_page(login_page_url)
    
    login_page = LogIn(driver)
    login_page.login()
    
    # Wait for the inventory page to load
    WebDriverWait(driver, 10).until(EC.url_contains("inventory.html"))

    # Check if the URL contains "inventory.html" keyword
    assert "inventory.html" in driver.current_url, "Failed to login"