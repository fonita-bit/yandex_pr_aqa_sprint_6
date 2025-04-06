import pytest
from pages.order_page import OrderPage
from locators.order_page_locators import OrderLocators

@pytest.mark.parametrize("order_data, button_position", [
    (("Иван", "Иванов", "ул. Ленина, 1", "89991112233"), "top"),
    (("Ольга", "Смирнова", "ул. Гагарина, 5", "89994445566"), "bottom")
])
def test_order_positive_flow(driver, order_data, button_position):
    name, surname, address, phone = order_data
    order_page = OrderPage(driver)
    order_page.open()
    order_page.close_cookies_if_present()
    order_page.scroll_to_order_button(button_position)
    order_page.click_order_button(button_position)
    order_page.fill_order_form(name, surname, address, phone)
    order_page.submit_order()
    order_button = driver.find_element(OrderLocators.ORDER_BUTTON)
    success_message = driver.find_element(OrderLocators.SUCCESS_MESSAGE)
    assert order_page.is_order_confirmed(), "Заказ не был подтвержден"