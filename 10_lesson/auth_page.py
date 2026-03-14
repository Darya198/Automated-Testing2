import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class AuthPage:
    """Класс для работы со страницей авторизации магазина SauceDemo"""

    def __init__(self, driver: WebDriver) -> None:
        """Инициализация драйвера и переход на страницу входа"""
        self._driver = driver
        self._driver.get('https://www.saucedemo.com/')
        self._driver.implicitly_wait(10)
        self._driver.maximize_window()

    @allure.step("Ввести логин 'standard_user' и пароль 'secret_sauce'")
    def login_and_password(self) -> None:
        """Вводит учетные данные и нажимает кнопку входа"""
        with allure.step("Ввод имени пользователя"):
            form = self._driver.find_element(
                By.CSS_SELECTOR, "input#user-name")
            form.clear()
            form.send_keys('standard_user')

        with allure.step("Ввод пароля"):
            form2 = self._driver.find_element(
                By.CSS_SELECTOR, "input#password")
            form2.clear()
            form2.send_keys('secret_sauce')

        with allure.step("Нажатие кнопки Login"):
            self._driver.find_element(By.CSS_SELECTOR,
                                      "input#login-button").click()
