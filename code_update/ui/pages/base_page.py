from selenium.common.exceptions import ElementClickInterceptedException
from ui.locators import basic_locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class PageNotOpenedExeption(Exception):
    pass


class BasePage(object):
    locators = basic_locators.BasePageLocators()
    url = 'https://target.my.com/'

    def is_opened(self, timeout=10):
        started = time.time()
        while time.time() - started < timeout:
            if self.driver.current_url == self.url:
                return True
        raise PageNotOpenedExeption(f'{self.url} did not open in {timeout} sec, current url {self.driver.current_url}')

    def __init__(self, driver):
        self.driver = driver

    def wait_element(self, timeout=None):
        if timeout is None:
            timeout = 15
        return WebDriverWait(self.driver, timeout=timeout)

    def find_element(self, locator, timeout=None):
        return self.wait_element(timeout).until(EC.presence_of_element_located(locator))

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    def click_on_element(self, locator, timeout=None):
        self.find_element(locator, timeout=timeout)
        CLICK_RETRY = 3
        while CLICK_RETRY > 0:
            try:
                elem = self.wait_element(timeout).until(EC.element_to_be_clickable(locator))
                elem.click()
                return
            except ElementClickInterceptedException:
                CLICK_RETRY = CLICK_RETRY - 1
                time.sleep(2)
