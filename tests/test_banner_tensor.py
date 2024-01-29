from selenium.webdriver.common.by import By
from pages.sbis import SbisPage


def test_banner_tensor(browser):
    sbis_page = SbisPage(browser)
    sbis_page.open_page()
    element = sbis_page.banner_tensor()
    browser.execute_script("arguments[0].click();", element)
    browser.switch_to.window(browser.window_handles[1])
    url = browser.current_url
    assert url == 'https://tensor.ru/'
