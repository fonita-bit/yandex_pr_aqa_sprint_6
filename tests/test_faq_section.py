import pytest
from pages.faq_page import FaqPage


@pytest.mark.parametrize("index", list(range(8)))
def test_faq_question_expansion(driver, index):
    faq_page = FaqPage(driver)
    faq_page.open()
    faq_page.close_cookies_if_present()
    faq_page.scroll_to_question(index)
    faq_page.expand_question(index)
    text = faq_page.get_answer_text(index)
    assert text != "", f"Ответ для вопроса {index} не отобразился"