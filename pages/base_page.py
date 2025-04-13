import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

    @allure.step("Кликаем по <body>")
    def click_body(self):
        body = self.driver.find_element(By.TAG_NAME, 'body')
        self.safe_click(body)

    @allure.step("Ждём, пока элемент с локатором {locator} исчезнет")
    def wait_until_invisible(self, locator, timeout=5):
        self.wait(timeout).until(EC.invisibility_of_element_located(locator))


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
    def close_popup_if_present(self, locator, timeout=10):  # Добавлено
        try:
            self.wait.until(EC.element_to_be_clickable(locator)).click()
        except Exception as e:
            print(f"Не удалось закрыть всплывающее окно: {e}")

    @allure.step("Выполняем JavaScript: {script}")
    def execute_script(self, script):  # Добавлено
        return self.driver.execute_script(script)

    @allure.step("Кликаем по элементу через JS: {locator}")
    def click_by_js(self, locator):  # Добавлено
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Безопасный клик по элементу: {locator}")
    def safe_click(self, locator):  # Добавлено
        try:
            self.wait_and_click(locator)
        except Exception:
            self.click_by_js(locator)
