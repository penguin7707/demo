from ui.locators import basic_locators
from ui.pages.base_page import BasePage
from ui.pages.main_page import MainPage


class LoginPage(BasePage):
    url = 'https://target.my.com/'

    def login(self, user, password):
        self.click_on_element(basic_locators.BasePageLocators.LOGIN_BUTTON_LOCATOR)
        login = self.find_element(basic_locators.BasePageLocators.LOGIN_EMAIL)
        login.clear()
        login.send_keys(user)
        pasword = self.find_element(basic_locators.BasePageLocators.LOGIN_PASSWORD)
        pasword.clear()
        pasword.send_keys(password)
        self.click_on_element(basic_locators.BasePageLocators.LOGIN_BUTTON2_LOCATOR)
        return MainPage(self.driver)



