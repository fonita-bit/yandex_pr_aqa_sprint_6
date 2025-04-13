import allure
from selenium.webdriver.common.by import By
from locators.order_page_locators import OrderLocators
from pages.base_page import BasePage
from urls import BASE_URL


class OrderPage(BasePage):

    # УДАЛЕНО: метод open с прямым обращением к self.driver
    # ДОБАВЛЕНО: использование open() из BasePage

    @allure.step("Открываем страницу оформления заказа")
    def open_order_page(self):  # новый метод с вызовом базового open()
        self.open(BASE_URL)

    @allure.step("Скроллим к кнопке заказа ({position})")
    def scroll_to_order_button(self, position):
        locator = OrderLocators.ORDER_BUTTON_TOP if position == "top" else OrderLocators.ORDER_BUTTON_BOTTOM
        self.scroll_to_element(locator)

    @allure.step("Кликаем по кнопке заказа ({position})")
    def click_order_button(self, position):
        locator = OrderLocators.ORDER_BUTTON_TOP if position == "top" else OrderLocators.ORDER_BUTTON_BOTTOM
        self.wait_and_click(locator)

    @allure.step("Заполняем первую форму заказа")
    def fill_first_order_form(self, name, surname, address, metro, phone):
        self.type(OrderLocators.FIRST_NAME, name)
        self.type(OrderLocators.LAST_NAME, surname)
        self.type(OrderLocators.ADDRESS, address)
        self.select_metro_station_by_name(metro)
        self.type(OrderLocators.PHONE, phone)

    @allure.step("Выбираем станцию метро по имени: {station_name}")
    def select_metro_station_by_name(self, station_name):
        self.wait_and_click(OrderLocators.METRO_INPUT)
        # ИСПРАВЛЕНО: локатор вынесен в метод
        metro_option_locator = (By.XPATH, f"//div[@class='select-search__select']//div[text()='{station_name}']")
        self.wait_and_click(metro_option_locator)

    @allure.step("Заполняем вторую форму заказа")
    def fill_second_order_form(self, delivery_date="10.04.2025", rental_period="сутки", color="black", comment="Позвоните заранее"):
        self.type(OrderLocators.DATE_INPUT, delivery_date)
        self.wait_and_click(OrderLocators.RENT_DROPDOWN)
        self.wait_and_click(OrderLocators.RENT_OPTION)
        self.wait_and_click(OrderLocators.SCOOTER_COLOR_BLACK if color == "black" else OrderLocators.SCOOTER_COLOR_GREY)
        self.type(OrderLocators.COMMENT_FIELD, comment)

    @allure.step("Подтверждаем заказ")
    def submit_order(self):
        self.wait_and_click(OrderLocators.NEXT_BUTTON)
        self.wait_and_click(OrderLocators.CONFIRM_BUTTON)

    @allure.step("Проверяем, что заказ подтвержден")
    def is_order_confirmed(self):
        return self.wait_for_visible(OrderLocators.ORDER_CONFIRMED)

    @allure.step("Закрываем попап куки")
    def close_cookies_if_present(self):
        if self.is_element_present(OrderLocators.COOKIES_CLOSE):
            self.wait_and_click(OrderLocators.COOKIES_CLOSE)

    @allure.step("Заполняем первую форму заказа")
    def fill_order_form_first_step(self, name, surname, address, metro, phone):
        self.type(OrderLocators.FIRST_NAME, name)
        self.type(OrderLocators.LAST_NAME, surname)
        self.type(OrderLocators.ADDRESS, address)
        self.select_metro_station_by_name(metro)
        self.type(OrderLocators.PHONE, phone)
        self.wait_and_click(OrderLocators.NEXT_BUTTON)

    @allure.step("Заполняем вторую форму заказа")
    def fill_order_form_second_step(self, date, rental, color, comment):
        self.close_cookies_if_present()
        self.scroll_to_element(OrderLocators.DATE_INPUT)
        self.type(OrderLocators.DATE_INPUT, date)

        # ⬇️ Новое: ждём исчезновения datepicker и кликаем по body, чтобы убрать перекрытие
        self.wait_until_invisible((By.CLASS_NAME, "react-datepicker"))
        self.click_body()  # метод добавим в base_page

        self.wait_and_click(OrderLocators.RENT_DROPDOWN)
        self.wait_and_click(OrderLocators.RENT_OPTION)

        if color == "black":
            self.wait_and_click(OrderLocators.SCOOTER_COLOR_BLACK)
        elif color == "grey":
            self.wait_and_click(OrderLocators.SCOOTER_COLOR_GREY)

        self.type(OrderLocators.COMMENT_FIELD, comment)
        self.scroll_to_element(OrderLocators.CONFIRM_BUTTON)
        self.wait_and_click(OrderLocators.CONFIRM_BUTTON)

    @allure.step("Переходим ко второму шагу оформления заказа")
    def go_to_second_step(self):
        self.click(OrderLocators.NEXT_BUTTON)
        self.wait_for_visible(OrderLocators.DATE_INPUT)