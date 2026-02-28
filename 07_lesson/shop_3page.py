from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    def __init__(self, driver):
        self._driver = driver
        self._driver.get('https://www.saucedemo.com/cart.html')
        self._driver.implicitly_wait(10)
        self._driver.maximize_window()

    def click_checkout(self):
        wait = WebDriverWait(self._driver, 50)
        wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "button#checkout"))).click()
