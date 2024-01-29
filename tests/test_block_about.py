from selenium.webdriver.common.by import By
from pages.tensor import TensorPage


def test_block_sila_v_ludyah(browser):
    sbis_page = TensorPage(browser)
    sbis_page.open_page()
    block_sila_v_ludyah = sbis_page.sila_v_ludyah()
    assert block_sila_v_ludyah.is_displayed()


def test_button_about(browser):
    tensor_page = TensorPage(browser)
    element = tensor_page.button_about()
    browser.execute_script("arguments[0].click();", element)
    url = browser.current_url
    assert url == 'https://tensor.ru/about'
