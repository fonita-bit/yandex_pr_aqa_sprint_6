import pytest
import allure
from pages.faq_page import FaqPage

@allure.suite("FAQ Блок")
class TestFaqSection:

    @allure.title("Проверка, что отображается ответ на вопрос {index}")
    @pytest.mark.parametrize("index", list(range(8)))
    def test_faq_question_expansion(self, driver, index):
        faq_page = FaqPage(driver)
        faq_page.open()
        faq_page.close_cookies_if_present()
        faq_page.scroll_to_question(index)
        faq_page.expand_question(index)
        answer = faq_page.get_answer_text(index)
        assert answer.strip() != "", f"Ответ на вопрос {index} не отобразился"