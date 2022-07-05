from ui.pages.base_page import BasePage
from ui.locators import basic_locators
from ui.pages.dashboard_page import DashboardPage
from ui.pages.segment_page import SegmentPage


class MainPage(BasePage):
    url = 'https://target.my.com/dashboard'
    locators = basic_locators.MainPage

    def go_to_segment_page(self):
        self.click_on_element(self.locators.SEGMENTS)
        return SegmentPage(self.driver)

    def go_to_dashboard_page(self):
        self.click_on_element(self.locators.DASHBOARD)
        return DashboardPage(self.driver)
