from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Page_calc:
    def __init__(self, driver):
        self._driver = driver
        self._driver.get('https://bonigarcia.dev/'
                         'selenium-webdriver-java/slow-calculator.html')
        self._driver.implicitly_wait(50)
        self._driver.maximize_window()

    def seconds(self):
        form = self._driver.find_element(By.CSS_SELECTOR, '#delay')
        form.clear()
        form.send_keys('45')

    def buttons(self):
        wait = WebDriverWait(self._driver, 50)
        self._driver.find_element(By.XPATH, "//span[text()='7']").click()
        self._driver.find_element(By.XPATH, "//span[text()='+']").click()
        self._driver.find_element(By.XPATH, "//span[text()='8']").click()
        self._driver.find_element(By.XPATH, "//span[text()='=']").click()
        wait.until(EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, ".screen"), "15"))
