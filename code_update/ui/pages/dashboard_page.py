import string
import random
from ui.pages.base_page import BasePage
from ui.locators import basic_locators


class DashboardPage(BasePage):
    url = 'https://target.my.com/dashboard'
    locators = basic_locators.DashboardPage

    def create_dashboard(self, file_path):
        self.click_on_element(self.locators.CREATE_DASHBOARD)
        self.click_on_element(self.locators.TRAFFIC)
        url_for_dashboard = self.find_element(self.locators.URL)
        url_for_dashboard.clear()
        url_for_dashboard.send_keys('https://target.my.com/')
        self.click_on_element(self.locators.FORMAT)
        name = self.find_element(self.locators.NAME)
        name.clear()
        letters = string.ascii_lowercase
        rand_string = ''.join(random.choice(letters) for i in range(8))
        name.send_keys(rand_string)
        self.find_element(self.locators.INPUT).send_keys(file_path)
        self.click_on_element(self.locators.SAVE_IMAGE)
        self.click_on_element(self.locators.CREATE)
        return '// a[contains(@title, "' + rand_string + '")]'