from pages.base import BasePage
from selenium.webdriver.common.by import By


button_xpath = (By.XPATH, '//*[@class="tensor_ru-link tensor_ru-Index__link" and @href="/about"]')
sila_v_ludyah_xpath = (By.XPATH, '(//*[text()="Сила в людях"])')


class TensorPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)


    def open_page(self):
        self.browser.get('https://tensor.ru/')


    def sila_v_ludyah(self):
        return self.find(sila_v_ludyah_xpath)


    def button_about(self):
        return self.find(button_xpath)
