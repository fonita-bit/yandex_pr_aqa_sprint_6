from selenium.webdriver.common.by import By

class OrderLocators:
    ORDER_BUTTON_TOP = (By.XPATH, "//button[text()='Заказать']")
    ORDER_BUTTON_BOTTOM = (By.XPATH, "//div[@class='Home_FinishButton__1_cWm']/button")
    FIRST_NAME = (By.XPATH, "//input[@placeholder='* Имя']")
    LAST_NAME = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    PHONE = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")

    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")
    DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")

    CONFIRM_BUTTON = (By.XPATH, "//button[text()='Да']")
    ORDER_CONFIRMED = (By.CLASS_NAME, "Order_ModalHeader")
    COOKIES_CLOSE = (By.ID, "rcc-confirm-button")
    ORDER_BUTTON = (By.XPATH, "//button[text()='Заказать']")
    SUCCESS_MESSAGE = (By.XPATH, "//div[@class='Order_ModalHeader__3FDaJ']/h3")
    METRO_INPUT = (By.CLASS_NAME, "select-search__input")  # Поле метро
    METRO_OPTION = (By.XPATH, "//li[@class='select-search__row']")  # Любая станция
#-- второго шага формы--
    DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENT_DROPDOWN = (By.CLASS_NAME, "Dropdown-control")
    RENT_OPTION = (By.XPATH, "//div[@class='Dropdown-option' and text()='сутки']")
    SCOOTER_COLOR_BLACK = (By.ID, "black")
    SCOOTER_COLOR_GREY = (By.ID, "grey")
    COMMENT_FIELD = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    CONFIRM_BUTTON = (By.XPATH, "//button[contains(text(), 'Заказать')]")
    ORDER_CONFIRMED = (By.XPATH, "//div[contains(text(), 'Заказ оформлен')]")

    @staticmethod
    def metro_option_by_name(station_name):
        return (By.XPATH, f"//div[@class='select-search__select']//div[text()='{station_name}']")