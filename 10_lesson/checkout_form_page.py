import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class CheckoutFormPage:
    """Класс для заполнения данных покупателя на этапе оформления заказа"""

    def __init__(self, driver: WebDriver) -> None:
        """Инициализация драйвера и переход на страницу ввода данных"""
        self._driver = driver
        self._driver.get('https://www.saucedemo.com/checkout-step-one.html')
        self._driver.implicitly_wait(10)
        self._driver.maximize_window()

    @allure.step("Заполнение формы покупателя: имя, фамилия, почтовый индекс")
    def fill_in(self) -> None:
        """Вводит данные пользователя в поля формы и нажимает 'Continue'"""
        wait = WebDriverWait(self._driver, 50)

        with allure.step("Ввод имени 'Иван'"):
            first_name = self._driver.find_element(
                By.CSS_SELECTOR, "input#first-name")
            first_name.clear()
            first_name.send_keys('Иван')

        with allure.step("Ввод фамилии 'Петров'"):
            last_name = self._driver.find_element(
                By.CSS_SELECTOR, "input#last-name")
            last_name.clear()
            last_name.send_keys('Петров')

        with allure.step("Ввод почтового индекса '123456'"):
            postal_code = self._driver.find_element(
                By.CSS_SELECTOR, "input#postal-code")
            postal_code.clear()
            postal_code.send_keys('123456')

        with allure.step("Нажатие кнопки Continue"):
            wait.until(EC.element_to_be_clickable((
                By.CSS_SELECTOR, "input#continue"))).click()
