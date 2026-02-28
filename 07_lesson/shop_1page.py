from selenium.webdriver.common.by import By


class MainPage:
    def __init__(self, driver):
        self._driver = driver
        self._driver.get('https://www.saucedemo.com/')
        self._driver.implicitly_wait(10)
        self._driver.maximize_window()

    def login_and_password(self):
        form = self._driver.find_element(By.CSS_SELECTOR, "input#user-name")
        form.clear()
        form.send_keys('standard_user')

        form2 = self._driver.find_element(
            By.CSS_SELECTOR, "input#password")
        form2.clear()
        form2.send_keys('secret_sauce')

        self._driver.find_element(By.CSS_SELECTOR,
                                  "input#login-button").click()
