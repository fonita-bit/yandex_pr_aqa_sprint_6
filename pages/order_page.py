from pages.base_page import BasePage

class OrderPage(BasePage):
    def open(self):
        self.driver.get("https://qa-scooter.praktikum-services.ru/")

    def scroll_to_order_button(self, position):
        locator = OrderLocators.ORDER_BUTTON_TOP if position == "top" else OrderLocators.ORDER_BUTTON_BOTTOM
        self.scroll_to_element(locator)

    def click_order_button(self, position):
        locator = OrderLocators.ORDER_BUTTON_TOP if position == "top" else OrderLocators.ORDER_BUTTON_BOTTOM
        self.wait_and_click(locator)

    def fill_order_form(self, name, surname, address, phone):
        self.type(OrderLocators.FIRST_NAME, name)
        self.type(OrderLocators.LAST_NAME, surname)
        self.type(OrderLocators.ADDRESS, address)
        self.type(OrderLocators.PHONE, phone)

    def submit_order(self):
        self.wait_and_click(OrderLocators.NEXT_BUTTON)
        self.wait_and_click(OrderLocators.CONFIRM_BUTTON)

    def is_order_confirmed(self):
        return self.wait_for_visible(OrderLocators.ORDER_CONFIRMED)

    def close_cookies_if_present(self):
        if self.is_element_present(OrderLocators.COOKIES_CLOSE):
            self.wait_and_click(OrderLocators.COOKIES_CLOSE)