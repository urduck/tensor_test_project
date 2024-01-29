import pytest
from selenium import webdriver


@pytest.fixture(scope="module")
def browser():
    chrome_browser = webdriver.Chrome()
    chrome_browser.implicitly_wait(20)
    return chrome_browser
