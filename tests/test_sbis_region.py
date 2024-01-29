from selenium.webdriver.common.by import By
from pages.sbis_region import SbisRegionPage
import time


my_region = 'Республика Татарстан'
kamchatskij_kraj_url = 'https://sbis.ru/contacts/41-kamchatskij-kraj?tab=clients'
kamchatskij_kraj_title = 'Камчатский край'


def test_sbis_my_region(browser):
    sbis_region = SbisRegionPage(browser)
    sbis_region.open_page()
    element_region = sbis_region.region()
    assert element_region.text == my_region


def test_sbis_contacts(browser):
    sbis_contacts = SbisRegionPage(browser)
    element_contacts = sbis_contacts.region()
    assert element_contacts.is_displayed()


def test_change_region(browser):
    sbis_region = SbisRegionPage(browser)
    sbis_region.click_region()
    sbis_region.click_kamchatskij_kraj()
    time.sleep(3)
    url = browser.current_url
    title = browser.title
    assert url == kamchatskij_kraj_url and kamchatskij_kraj_title in title



