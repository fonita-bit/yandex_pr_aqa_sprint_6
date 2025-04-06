from locators.faq_page_locators import FaqLocators
from pages.base_page import BasePage

class FaqPage(BasePage):
    def open(self):
        self.driver.get("https://qa-scooter.praktikum-services.ru/")

    def scroll_to_question(self, index):
        self.scroll_to_element(FaqLocators.QUESTION[index])

    def expand_question(self, index):
        self.wait_and_click(FaqLocators.QUESTION[index])

    def get_answer_text(self, index):
        return self.wait_for_visible(FaqLocators.ANSWER[index]).text

    def close_cookies_if_present(self):
        if self.is_element_present(FaqLocators.COOKIES_CLOSE):
            self.wait_and_click(FaqLocators.COOKIES_CLOSE)