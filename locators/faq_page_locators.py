from selenium.webdriver.common.by import By

class FaqLocators:
    QUESTION = [(By.ID, f"accordion__heading-{i}") for i in range(8)]
    ANSWER = [(By.ID, f"accordion__panel-{i}") for i in range(8)]
    COOKIES_CLOSE = (By.ID, "rcc-confirm-button")