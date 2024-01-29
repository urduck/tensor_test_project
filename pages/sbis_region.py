from pages.base import BasePage
from selenium.webdriver.common.by import By


region_xpath = (By.XPATH, '//*[@class="sbis_ru-Region-Chooser__text sbis_ru-link"]')
contacts_xpath = (By.XPATH, '//*[@id="contacts_list"]')
kamchatskij_kraj_xpath = (By.XPATH, '//*[text()="41 Камчатский край"]')


class SbisRegionPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)


    def open_page(self):
        self.browser.get('https://sbis.ru/contacts')


    def region(self):
        return self.find(region_xpath)


    def contacts(self):
        return self.find(contacts_xpath)


    def click_region(self):
        return self.find(region_xpath).click()


    def click_kamchatskij_kraj(self):
        return self.find(kamchatskij_kraj_xpath).click()


