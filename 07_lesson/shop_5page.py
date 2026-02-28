from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LastPage:
    def __init__(self, driver):
        self._driver = driver
        self._driver.get('https://www.saucedemo.com/checkout-step-two.html')
        self._driver.implicitly_wait(10)
        self._driver.maximize_window()

    def price(self):
        wait = WebDriverWait(self._driver, 50)
        price_total_text = wait.until(EC.presence_of_element_located((
            By.CSS_SELECTOR, ".summary_total_label"))).text
        return price_total_text
