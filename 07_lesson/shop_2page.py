from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SearchPage:
    def __init__(self, driver):
        self._driver = driver
        self._driver.get('https://www.saucedemo.com/inventory.html')
        self._driver.implicitly_wait(10)
        self._driver.maximize_window()

    def add_items(self):
        wait = WebDriverWait(self._driver, 50)
        wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "button#add-to-cart-sauce-labs-backpack")
            )).click()
        wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "button#add-to-cart-sauce-labs-bolt-t-shirt")
            )).click()
        wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "button#add-to-cart-sauce-labs-onesie")
            )).click()
