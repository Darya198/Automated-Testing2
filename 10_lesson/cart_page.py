import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class CartPage:
    """Класс для работы со страницей корзины SauceDemo"""

    def __init__(self, driver: WebDriver) -> None:
        """Инициализация драйвера и переход в корзину"""
        self._driver = driver
        self._driver.get('https://www.saucedemo.com/cart.html')
        self._driver.implicitly_wait(10)
        self._driver.maximize_window()

    @allure.step("Нажатие кнопки 'Checkout' для перехода к оформлению заказа")
    def click_checkout(self) -> None:
        """Ожидает доступности кнопки оформления заказа и нажимает на неё"""
        wait = WebDriverWait(self._driver, 50)

        with allure.step("Клик по кнопке Checkout"):
            wait.until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "button#checkout"))).click()
