from selenium.webdriver.common.by import By
from pages.tensor_about import TensorPage, check_size
import time


def test_image_size(browser):
    sbis_page = TensorPage(browser)
    sbis_page.open_page()
    objects_sizes = []
    time.sleep(3)
    elements = browser.find_elements(By.CLASS_NAME, 'tensor_ru-About__block3-image-wrapper')

    for element, i in enumerate(elements):
        img = browser.find_element(By.TAG_NAME, 'img')
        width = int(img.size['width'])
        height = int(img.size['height'])
        object_sizes = [width, height]
        objects_sizes.append(object_sizes)

    assert check_size(objects_sizes)
