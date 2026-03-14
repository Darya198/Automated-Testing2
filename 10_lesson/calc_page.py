import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class Page_calc:
    """Класс для работы со страницей медленного калькулятора"""

    def __init__(self, driver: WebDriver) -> None:
        """Инициализация драйвера и открытие страницы"""
        self._driver = driver
        self._driver.get('https://bonigarcia.dev/'
                         'selenium-webdriver-java/slow-calculator.html')
        self._driver.implicitly_wait(50)
        self._driver.maximize_window()

    @allure.step("Установка задержки выполнения в 45 секунд")
    def seconds(self) -> None:
        """Очищение поля задержки и ввод значения 45"""
        form = self._driver.find_element(By.CSS_SELECTOR, '#delay')
        form.clear()
        form.send_keys('45')

    @allure.step("Нажатие кнопок: 7, +, 8, = и ожидание результата")
    def buttons(self) -> None:
        """Выполнение сложения 7 + 8 и ожидание появления результата 15"""
        wait = WebDriverWait(self._driver, 50)
        self._driver.find_element(By.XPATH, "//span[text()='7']").click()
        self._driver.find_element(By.XPATH, "//span[text()='+']").click()
        self._driver.find_element(By.XPATH, "//span[text()='8']").click()
        self._driver.find_element(By.XPATH, "//span[text()='=']").click()

        # Ожидание текста в элементе
        wait.until(EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, ".screen"), "15"))
