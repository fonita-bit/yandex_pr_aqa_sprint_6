import pytest
import allure
from pages.order_page import OrderPage
from test_data import valid_orders

@allure.suite("Проверка сценария заказа самоката")
class TestOrderFlow:

    @allure.title("Проверка заказа самоката: {data}")
    @pytest.mark.parametrize("order_data, position", valid_orders)
    def test_order_flow(self, driver, order_data, position):
        order_page = OrderPage(driver)
        order_page.open()

        # Прокручиваем страницу и кликаем кнопку в зависимости от позиции
        order_page.scroll_to_order_button(position)
        order_page.click_order_button(position)

        # Заполняем первую форму
        order_page.fill_first_order_form(*order_data[:5])
        # передаем имя, фамилию, адрес, метро, телефон
        order_page.go_to_second_step()
        order_page.fill_second_order_form(*order_data[5:8])
        # передаем дату, срок аренды, цвет
        order_page.submit_order()
        #print("Переход к заполнению второй формы...")
        # Проверка, что заказ оформлен
        assert order_page.is_order_confirmed(), "Заказ не был подтвержден"
