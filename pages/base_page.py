from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators.base_page_locators import BasePageLocators

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    @allure.step("Открываем URL: {url}")
    def open(self, url):
        self.driver.get(url)

    @allure.step("Ожидаем, пока элемент не станет видимым: {locator}")
    def wait_for_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Кликаем по элементу: {locator}")
    def wait_and_click(self, locator):
        element = self.wait_for_visible(locator)
        element.click()

    @allure.step("Вводим текст '{text}' в поле: {locator}")
    def type(self, locator, text):
        element = self.wait_for_visible(locator)
        element.clear()
        element.send_keys(text)

    @allure.step("Прокручиваем страницу до элемента: {locator}")
    def scroll_to_element(self, locator):
        element = self.wait_for_visible(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Проверяем, присутствует ли элемент: {locator}")
    def is_element_present(self, locator):
        try:
            self.wait.until(EC.presence_of_element_located(locator))
            return True
        except:
            return False

    @allure.step("Кликаем по элементу: {locator}")
    def click(self, locator):
        self.wait_and_click(locator)

    @allure.step("Получаем текущий URL")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Переключаемся на последнюю вкладку")
    def switch_to_last_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    @allure.step("Закрываем всплывающее окно, если оно присутствует")
    def close_popup_if_present(self, timeout=10):
        try:
            popup_close_button = (By.XPATH, "//button[contains(@class, 'popup-close')]")
            WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(popup_close_button)
            ).click()
        except Exception as e:
            print(f"Не удалось закрыть всплывающее окно: {e}")