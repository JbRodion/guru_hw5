import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_duck_search_selenium(driver):
    driver.get('https://duckduckgo.com/')

    search_box = driver.find_element(By.NAME,'q')
    search_box.send_keys('selene github')
    search_box.send_keys(Keys.ENTER)

    expected_text = 'GitHub - FunctionLab/selene: a framework for training sequence-level ...'\

    h2_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.TAG_NAME, 'h2'))
    )

    assert h2_element.text == expected_text

def test_google_search_selene():
    pass