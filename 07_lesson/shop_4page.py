from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FormPage:
    def __init__(self, driver):
        self._driver = driver
        self._driver.get('https://www.saucedemo.com/checkout-step-one.html')
        self._driver.implicitly_wait(10)
        self._driver.maximize_window()

    def fill_in(self):
        wait = WebDriverWait(self._driver, 50)
        form = self._driver.find_element(
            By.CSS_SELECTOR, "input#first-name")
        form.clear()
        form.send_keys('Иван')

        form = self._driver.find_element(
            By.CSS_SELECTOR, "input#last-name")
        form.clear()
        form.send_keys('Петров')

        form = self._driver.find_element(
            By.CSS_SELECTOR, "input#postal-code")
        form.clear()
        form.send_keys('123456')

        wait.until(EC.element_to_be_clickable((
            By.CSS_SELECTOR, "input#continue"))).click()
