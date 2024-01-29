from pages.base import BasePage
from selenium.webdriver.common.by import By


button_xpath = (By.XPATH, '//*[@class="tensor_ru-link tensor_ru-Index__link" and @href="/about"]')


def check_size(obj_sizes):
    for i in range(0, len(obj_sizes)-1):
        if obj_sizes[i][0] != obj_sizes[i+1][0] or obj_sizes[i][1] != obj_sizes[i+1][1]:
            return False
    return True


class TensorPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)


    def open_page(self):
        self.browser.get('https://tensor.ru/about')


    def button_about(self):
        return self.find(button_xpath)
