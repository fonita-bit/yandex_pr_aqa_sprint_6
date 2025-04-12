import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.order_page_locators import OrderLocators
from pages.base_page import BasePage
from urls import BASE_URL


class OrderPage(BasePage):

    @allure.step("Открываем страницу оформления заказа")
    def open(self):
        self.driver.get(BASE_URL)

    @allure.step("Скроллим к кнопке заказа ({position})")
    def scroll_to_order_button(self, position):
        locator = OrderLocators.ORDER_BUTTON_TOP if position == "top" else OrderLocators.ORDER_BUTTON_BOTTOM
        self.scroll_to_element(locator)

    @allure.step("Кликаем по кнопке заказа ({position})")
    def click_order_button(self, position):
        locator = OrderLocators.ORDER_BUTTON_TOP if position == "top" else OrderLocators.ORDER_BUTTON_BOTTOM
        self.wait_and_click(locator)

    @allure.step("Заполняем первую форму заказа")
    def fill_first_order_form(self, name, surname, address, metro,phone):
        self.type(OrderLocators.FIRST_NAME, name)
        self.type(OrderLocators.LAST_NAME, surname)
        self.type(OrderLocators.ADDRESS, address)
        self.select_metro_station_by_name(metro)
        self.type(OrderLocators.PHONE, phone)

    @allure.step("Выбираем станцию метро по имени: {station_name}")
    def select_metro_station_by_name(self, station_name):
        self.wait_and_click(OrderLocators.METRO_INPUT)
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
        # Скрытие элемента календаря
        self.driver.execute_script("document.querySelector('.react-datepicker').style.display = 'none';")
        # Закрываем календарь с помощью JavaScript (кликаем по элементу для закрытия)
        try:
            # Кликаем по элементу с классом 'Order_Header__BZXOb' для закрытия календаря
            self.driver.execute_script("document.querySelector('.Order_Header__BZXOb').click();")
            print("Календарь был закрыт кликом по элементу для аренды.")
        except Exception as e:
            print(f"Не удалось закрыть календарь с помощью JavaScript: {str(e)}")

        # Ожидаем, пока исчезнет календарь, и потом кликаем по полю "Срок аренды"
        self.driver.execute_script("document.querySelector('.Dropdown-placeholder').click();")
        print("Выбрано поле 'Срок аренды' для выбора.")

        # Кликаем на выпадающий список для выбора срока аренды
        self.wait_and_click(OrderLocators.RENT_DROPDOWN)

        self.safe_click(OrderLocators.RENT_OPTION)

        if color == "black":
            self.safe_click(OrderLocators.SCOOTER_COLOR_BLACK)
        elif color == "grey":
            self.safe_click(OrderLocators.SCOOTER_COLOR_GREY)

        self.type(OrderLocators.COMMENT_FIELD, comment)
        self.scroll_to_element(OrderLocators.CONFIRM_BUTTON)
        self.safe_click(OrderLocators.CONFIRM_BUTTON)

    @allure.step("Переходим ко второму шагу оформления заказа")
    def go_to_second_step(self):
        self.click(OrderLocators.NEXT_BUTTON)  # нажимаем "Далее"
        self.wait_for_visible(
            OrderLocators.DATE_INPUT)  # ждём появления поля даты (или другого уникального элемента второго шага)
