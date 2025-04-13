import pytest
from selene import browser
from selenium.webdriver.chrome import webdriver


@pytest.fixture(scope='function')
def browser_options():

    browser.config.base_url = 'https://demoqa.com'
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    driver_options = webdriver.ChromeOptions()

    yield

    browser.quit()