import pytest
import allure
from pages.order_page import OrderPage
from test_data import valid_orders


@allure.suite("Позитивные проверки оформления заказа")
class TestOrderFlow:

    @pytest.mark.parametrize("order_data, button_position", valid_orders)
    @allure.title("Успешное оформление заказа через кнопку {button_position}")
    def test_order_positive_flow(self, driver, order_data, button_position):
        (
            name, surname, address, metro, phone,
            date, rental_period, color, comment
        ) = order_data

        order_page = OrderPage(driver)
        order_page.open()
        order_page.close_cookies_if_present()
        order_page.scroll_to_order_button(button_position)
        order_page.click_order_button(button_position)

        # Первый шаг формы
        order_page.fill_order_form_first_step(name, surname, address, metro, phone)

        # Второй шаг формы
        order_page.fill_order_form_second_step(date, rental_period, color, comment)

        assert order_page.is_order_confirmed(), "Заказ не был подтвержден"