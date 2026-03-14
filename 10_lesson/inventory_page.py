import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class InventoryPage:
    """Класс для работы с витриной товаров SauceDemo"""

    def __init__(self, driver: WebDriver) -> None:
        """Инициализация драйвера и переход на страницу товаров."""
        self._driver = driver
        # Ссылка уже открывается после логина, но оставим для надежности
        self._driver.get('https://www.saucedemo.com/inventory.html')
        self._driver.implicitly_wait(10)
        self._driver.maximize_window()

    @allure.step("Добавление трех товаров в корзину:"
                 "рюкзак, футболку и комбинезон")
    def add_items(self) -> None:
        """Находит и кликает кнопки добавления товаров в корзину"""
        wait = WebDriverWait(self._driver, 50)

        with allure.step("Добавить Sauce Labs Backpack"):
            wait.until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "button#add-to-cart-sauce-labs-backpack")
            )).click()

        with allure.step("Добавить Sauce Labs Bolt T-Shirt"):
            wait.until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "button#add-to-cart-sauce-labs-bolt-t-shirt")
            )).click()

        with allure.step("Добавить Sauce Labs Onesie"):
            wait.until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "button#add-to-cart-sauce-labs-onesie")
            )).click()
