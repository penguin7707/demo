import time
import pytest
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import ElementClickInterceptedException
from ui.locators import basic_locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseCase:
    driver = None

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver):
        self.driver = driver

    def wait_element(self, timeout=None):
        if timeout is None:
            timeout = 10
        return WebDriverWait(self.driver, timeout=timeout)

    def find_element(self, locator, timeout=None):
        return self.wait_element(timeout).until(EC.presence_of_element_located(locator))

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    def click_on_element(self, locator, timeout=None) -> WebElement:
        self.find_element(locator, timeout=timeout)
        CLICK_RETRY = 3
        while CLICK_RETRY > 0:
            try:
                elem = self.wait_element(timeout).until(EC.element_to_be_clickable(locator))
                elem.click()
                return
            except ElementClickInterceptedException:
                CLICK_RETRY = CLICK_RETRY - 1

    def log_in(self, user_email, user_password):
        self.click_on_element(basic_locators.LOGIN_BUTTON_LOCATOR)
        email = self.find_element(basic_locators.LOGIN_EMAIL)
        email.send_keys(user_email)
        password = self.find_element(basic_locators.LOGIN_PASSWORD)
        password.send_keys(user_password)
        self.click_on_element(basic_locators.LOGIN_BUTTON2_LOCATOR)
        '''Ожидание загрузки страницы для других тестов'''
        self.find_element(basic_locators.LOGIN)

    def log_out(self):
        self.click_on_element(basic_locators.LOGOUT_BUTTON1_LOCATOR)
        self.click_on_element(basic_locators.LOGOUT_BUTTON2_LOCATOR)

    def change_info(self, user_name, user_phone, user_email):
        self.click_on_element(basic_locators.PROFILE_BUTTON)

        self.click_on_element(basic_locators.MORE_BUTTON)

        name_phone_email = self.find_elements(basic_locators.NAME_PHONE_EMAIL)
        name_phone_email[0].clear()
        name_phone_email[0].send_keys(user_name)

        name_phone_email[1].clear()
        name_phone_email[1].send_keys(user_phone)

        name_phone_email[2].clear()
        name_phone_email[2].send_keys(user_email)

        self.click_on_element(basic_locators.DELETE_BUTTON)

        self.click_on_element(basic_locators.SAVE_BUTTON)

