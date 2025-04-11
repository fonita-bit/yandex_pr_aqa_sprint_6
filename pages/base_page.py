from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators.base_page_locators import BasePageLocators

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def open(self, url):  #  Унифицированный open()
        self.driver.get(url)

    def wait_for_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_and_click(self, locator):
        element = self.wait_for_visible(locator)
        element.click()

    def type(self, locator, text):
        element = self.wait_for_visible(locator)
        element.clear()
        element.send_keys(text)

    def scroll_to_element(self, locator):
        element = self.wait_for_visible(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def is_element_present(self, locator):
        try:
            self.wait.until(EC.presence_of_element_located(locator))
            return True
        except:
            return False

    def click(self, locator):
        self.wait_and_click(locator)

    def get_current_url(self):
        return self.driver.current_url

    def switch_to_last_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def click_yandex_logo(self):
        self.wait_and_click(BasePageLocators.YANDEX_LOGO)

    def click_scooter_logo(self):
        self.wait_and_click(BasePageLocators.SCOOTER_LOGO)

    def select(self, input_locator, value_locator):
        # Кликаем на поле и выбираем из списка
        self.wait_and_click(input_locator)
        self.wait_and_click(value_locator)

    def safe_click(self, locator):
        self.scroll_to_element(locator)
        element = self.wait_for_clickable(locator)
        element.click()

    def wait_for_clickable(self, locator, timeout=10):
        """
        Ожидаем, пока элемент не станет доступным для клика.
        """
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    def close_popup_if_present(self, timeout=10):
        """
        Пытаемся закрыть всплывающее окно, если оно присутствует.
        Используем стандартный локатор для закрытия окон, но можно адаптировать под ваш сайт.
        """
        try:
            # Пример локатора для закрытия всплывающего окна (может отличаться на вашем сайте)
            popup_close_button = (By.XPATH, "//button[contains(@class, 'popup-close')]")  # Замените XPATH на подходящий
            WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(popup_close_button)
            ).click()
            print("Всплывающее окно закрыто.")
        except Exception as e:
            print(f"Не удалось закрыть всплывающее окно: {e}")

