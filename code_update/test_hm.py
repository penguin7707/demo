import os
import allure
import pytest
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from base import BaseCase
from ui.pages.base_page import PageNotOpenedExeption


class Test_Negative(BaseCase):
    authorize = False

    @pytest.mark.UI
    @allure.step('Negative authorization test with invalid login')
    def test_lk1(self):
        self.login_page.login('alena199799@gmail.com', 'tWz+H@&Gws#Yj7L')
        with pytest.raises(PageNotOpenedExeption):
            self.login_page.is_opened()

    @pytest.mark.UI
    @allure.step('Negative authorization test with invalid password')
    def test_lk2(self):
        self.login_page.login('alena1997999@gmail.com', 'tWz+H@&Gws#Yj7')
        with pytest.raises(PageNotOpenedExeption):
            self.login_page.is_opened()


class Test_positive(BaseCase):

    @pytest.mark.UI
    @allure.step('Segment delete test (a segment with a unique name is created and then deleted)')
    def test_delete_segment(self):
        self.main_page.go_to_segment_page()
        self.segment_page.is_opened()
        segment_1 = self.segment_page.create_segment()
        segment = self.segment_page.delete_segment(segment_1)
        with pytest.raises(TimeoutException):
            self.segment_page.find_element((By.XPATH, segment))

    @pytest.mark.UI
    @allure.step('Segment create test (a segment with a unique name is created)')
    def test_create_segment(self):
        self.main_page.go_to_segment_page()
        self.segment_page.is_opened()
        segment = self.segment_page.create_segment()
        assert self.segment_page.find_element((By.XPATH, segment))
        self.segment_page.delete_segment(segment)

    @pytest.fixture()
    def file_path(self, repo_root):
        return os.path.join(repo_root, 'files', 'userdata.jpg')

    @pytest.mark.UI
    @allure.step('Traffic dashboard create test (a dashboard with a unique name is created)')
    def test_create_dashboard(self, file_path):
        self.dashboard_page.is_opened()
        dashboard = self.dashboard_page.create_dashboard(file_path)
        assert self.dashboard_page.find_element((By.XPATH, dashboard))
