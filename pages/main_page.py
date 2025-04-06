from locators.main_page_locators import MainPageLocators
from locators.base_page_locators import BasePageLocators
from pages.base_page import BasePage

class MainPage(BasePage):
    def click_top_order_button(self):
        self.click(MainPageLocators.ORDER_BUTTON_TOP)

    def click_bottom_order_button(self):
        self.click(MainPageLocators.ORDER_BUTTON_BOTTOM)
