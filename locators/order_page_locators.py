from selenium.webdriver.common.by import By

class OrderLocators:
    ORDER_BUTTON_TOP = (By.XPATH, "//button[text()='Заказать']")
    ORDER_BUTTON_BOTTOM = (By.XPATH, "//div[@class='Home_FinishButton__1_cWm']/button")
    FIRST_NAME = (By.XPATH, "//input[@placeholder='* Имя']")
    LAST_NAME = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    PHONE = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")
    CONFIRM_BUTTON = (By.XPATH, "//button[text()='Да']")
    ORDER_CONFIRMED = (By.CLASS_NAME, "Order_ModalHeader")
    COOKIES_CLOSE = (By.ID, "rcc-confirm-button")
    ORDER_BUTTON = (By.XPATH, "//button[text()='Заказать']")
    SUCCESS_MESSAGE = (By.XPATH, "//div[@class='Order_ModalHeader__3FDaJ']/h3")