from pages.base import BasePage
from selenium.webdriver.common.by import By


banner_xpath = (By.XPATH, '//*[@class="sbisru-Contacts__logo-tensor mb-12"]')


class SbisPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)


    def open_page(self):
        self.browser.get('https://sbis.ru/contacts')


    def banner_tensor(self):
        return self.find(banner_xpath)



