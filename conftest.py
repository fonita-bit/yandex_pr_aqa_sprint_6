import pytest
from selenium import webdriver
import os

@pytest.fixture
def driver(request):
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    yield driver
    if request.node.rep_call.failed:
        screenshot_path = f"screenshots/{request.node.name}.png"
        os.makedirs(os.path.dirname(screenshot_path), exist_ok=True)
        driver.save_screenshot(screenshot_path)
    driver.quit()

def pytest_runtest_makereport(item, call):
    if "driver" in item.fixturenames:
        driver = item.funcargs["driver"]
        if call.when == "call":
            item._request.node.rep_call = call

# Сохраняем результат каждого вызова
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
@pytest.fixture
def close_popups(browser):
    try:
        cookie_btn = browser.find_element("id", "rcc-confirm-button")
        browser.execute_script("arguments[0].scrollIntoView(true);", cookie_btn)
        cookie_btn.click()
    except:
        pass