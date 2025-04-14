import allure
import pytest
from pages.faq_page import FaqPage
from urls import BASE_URL  #  Централизованный BASE_URL


@allure.suite("Редиректы по логотипам")
class TestLogoRedirects:

    @allure.title("Проверка перехода по логотипу Самоката на главную страницу")
    def test_redirect_to_main_by_scooter_logo(self, driver):
        page = FaqPage(driver)
        page.open(BASE_URL)
        page.click_scooter_logo()
        assert BASE_URL in page.get_current_url(), "Переход по логотипу Самоката не ведёт на главную"

    @allure.title("Проверка редиректа по логотипу Яндекса на Dzen")
    def test_redirect_to_yandex_dzen(self, driver):
        page = FaqPage(driver)
        page.open(BASE_URL)
        page.click_yandex_logo()
        page.switch_to_last_tab()
        current_url = page.get_current_url()
        assert "dzen.ru" in current_url or "ya.ru" in current_url, "Редирект по логотипу Яндекса не ведёт на Dzen"
