import allure
from locators.base_page_locators import BasePageLocators
from locators.faq_page_locators import FaqLocators
from pages.base_page import BasePage
from urls import BASE_URL

class FaqPage(BasePage):

    @allure.step("Закрываем попап куки если он есть")
    def close_cookies_if_present(self):
        if self.is_element_present(FaqLocators.COOKIES_CLOSE):
            self.wait_and_click(FaqLocators.COOKIES_CLOSE)

    @allure.step("Скроллим к вопросу №{index}")
    def scroll_to_question(self, index):
        self.scroll_to_element(FaqLocators.QUESTION[index])

    @allure.step("Раскрываем вопрос №{index}")
    def expand_question(self, index):
        self.wait_and_click(FaqLocators.QUESTION[index])

    @allure.step("Получаем текст ответа на вопрос №{index}")
    def get_answer_text(self, index):
        return self.wait_for_visible(FaqLocators.ANSWER[index]).text

    @allure.step("Закрываем попап куки если он есть")
    def close_cookies_if_present(self):
        if self.is_element_present(FaqLocators.COOKIES_CLOSE):
            self.wait_and_click(FaqLocators.COOKIES_CLOSE)

    @allure.step("Кликаем по логотипу Самоката")
    def click_scooter_logo(self):
        self.click(BasePageLocators.SCOOTER_LOGO)

    @allure.step("Кликаем по логотипу Яндекс Дзена")
    def click_yandex_logo(self):
        self.click(BasePageLocators.YANDEX_LOGO)