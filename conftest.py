import pytest
from selenium import webdriver


@pytest.fixture(scope="module")
def browser():
    driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    return driver
