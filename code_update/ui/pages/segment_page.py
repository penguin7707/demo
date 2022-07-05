import string
import random
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from ui.pages.base_page import BasePage
from ui.locators import basic_locators


class SegmentPage(BasePage):
    url = 'https://target.my.com/segments/segments_list'
    locators = basic_locators.SegmentPage

    def create_segment(self):
        try:
            self.click_on_element(self.locators.CREATE_BUTTON1)
        except TimeoutException:
            self.click_on_element(self.locators.CREATE_BUTTON2)
        self.click_on_element(self.locators.SEGMENT_TYPE)
        self.click_on_element(self.locators.MORE_BUTTON)
        self.click_on_element(self.locators.PAID_BUTTON)
        self.click_on_element(self.locators.ADD_SEGMENT)
        segment_name = self.find_element(self.locators.SEGMENT_NAME)
        segment_name.clear()
        letters = string.ascii_lowercase
        rand_string = ''.join(random.choice(letters) for i in range(8))
        segment_name.send_keys(rand_string)
        self.click_on_element(self.locators.CREATE_SEGMENT)
        segment_locator = '//a[contains(@title, "' + rand_string + '")]'
        return segment_locator

    def delete_segment(self, segment_info):
        name_locator = segment_info + '/../../..//div/div/input'
        self.click_on_element((By.XPATH, name_locator))
        self.click_on_element(self.locators.DO_BUTTON)
        self.click_on_element(self.locators.DELETE_BUTTON)
        return name_locator
