from locators.main_page_locators import MainPageLocators
from locators.base_page_locators import BasePageLocators
from pages.base_page import BasePage

class MainPage(BasePage):
    @allure.step("Кликаем по кнопке заказа сверху")
    def click_top_order_button(self):
        self.click(MainPageLocators.ORDER_BUTTON_TOP)

    @allure.step("Кликаем по кнопке заказа снизу")
    def click_bottom_order_button(self):
        self.click(MainPageLocators.ORDER_BUTTON_BOTTOM)
