"""Helper Methods"""
import logging
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains

class GeneralHelpers:
    """General Helper methods"""
    def __init__(self, driver):
        self.driver = driver

    def go_to_page(self, url, new_window=False):
        """Method go to page"""
        if new_window:
            self.driver.execute_script(f"window.open('{url}');")
        else:
            self.driver.get(url)
            self.driver.maximize_window()

    def find_and_click(self, loc, timeout=10):
        """Find and click method"""
        elem = self.find(loc, timeout)
        elem.click()

    def find_and_send_keys(self, loc, inp_text, timeout=20):
        """Find and send keys method"""
        elem = self.find(loc, timeout)
        elem.send_keys(inp_text)

    def find(self, loc, timeout=20, should_exist=True, get_text="", get_attribute=""):
        """Find element method"""
        try:
            elem = WebDriverWait(self.driver, timeout).until(
                expected_conditions.presence_of_element_located(loc),
                message=f"Element '{loc}' not found!")
        except Exception as e_rror:
            self.logger(e_rror, error=True)
            if should_exist:
                raise Exception(e_rror)
            return False
        if get_text:
            return elem.text
        elif get_attribute:
            return elem.get_attribute(get_attribute)
        return elem

    def find_all(self, loc, timeout=10):
        """Find all elements method"""
        try:
            elements = WebDriverWait(self.driver, timeout).until(
                expected_conditions.presence_of_all_elements_located(loc),
                message=f"Elements '{loc}' not found!")
        except Exception as e_rror:
            self.logger(e_rror, error=True)
            return False
        return elements

    def wait_for_page(self, page="", not_page="", timeout=10):
        """Wait for page to load method"""
        if page:
            WebDriverWait(self.driver, timeout).until(
                expected_conditions.url_contains(page))
        elif not_page:
            WebDriverWait(self.driver, timeout).until_not(
                expected_conditions.url_contains(not_page))

    def switch_window(self, window_id=0):
        """Switch window method"""
        self.driver.switch_to.window(self.driver.window_handles[window_id])

    def switch_to_alert(self):
        """Smith cto alert method"""
        return self.driver.switch_to.alert

    def retrn_url(self):
        """Return url method"""
        return str(self.driver.current_url)

    def hover_elem(self, elem):
        """Hover element method"""
        a = ActionChains(self.driver)
        a.move_to_element(elem).perform()

    def logger(self, msg="", error=False):
        """Logger"""
        logging.basicConfig(
            filename='test_run.txt', filemode='a+',
            format='%(created)f - %(levelname)s - %(message)s',
            level=logging.INFO, force=True)
        if error:
            logging.error(msg)
        else:
            logging.info(msg)