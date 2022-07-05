import pytest
from ui.locators import basic_locators
from base import BaseCase


class Test_Target(BaseCase):

    @pytest.mark.UI
    def test_login(self):
        self.log_in('alena1997999@gmail.com', 'tWz+H@&Gws#Yj7L')
        assert 'Кампании' in self.driver.title

    @pytest.mark.UI
    def test_logout(self):
        self.log_in('alena1997999@gmail.com', 'tWz+H@&Gws#Yj7L')
        self.log_out()
        assert "Рекламная платформа" in self.driver.title

    @pytest.mark.UI
    def test_change_info(self):
        self.log_in('alena1997999@gmail.com', 'tWz+H@&Gws#Yj7L')
        self.change_info("Anna", "89069474448", "anna1234@test.com")
        assert 'Информация успешно сохранена' in self.driver.page_source

    @pytest.mark.UI
    @pytest.mark.parametrize(
        'page, expected',
        [
            pytest.param(
                basic_locators.CHANGE_PAGE1, 'Контактная информация'
            ),
            pytest.param(
                basic_locators.CHANGE_PAGE2, 'Лицевой счет'
            ),
        ],
    )
    def test_change_page(self, page, expected):
        self.log_in('alena1997999@gmail.com', 'tWz+H@&Gws#Yj7L')
        self.click_on_element(page)
        assert expected in self.driver.title


