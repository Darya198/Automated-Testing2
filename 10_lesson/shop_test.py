import pytest
import allure
from typing import Generator
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager

from auth_page import AuthPage
from inventory_page import InventoryPage
from cart_page import CartPage
from checkout_form_page import CheckoutFormPage
from checkout_summary_page import CheckoutSummaryPage


@pytest.fixture
def driver() -> Generator[WebDriver, None, None]:
    """Фикстура для инициализации драйвера Chrome"
    "с отключением лишних функций"""
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False
    }
    options.add_experimental_option("prefs", prefs)
    options.add_argument("--disable-features=AutofillServerCommunication")
    options.add_argument("--disable-features=PasswordManagerOnboarding")

    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    yield driver
    driver.quit()


@allure.feature("Интернет-магазин SauceDemo")
@allure.story("Оформление заказа")
@allure.title("Покупка нескольких товаров (рюкзак, футболка, комбинезон)")
@allure.description("Тест проверяет полный цикл:"
                    "от авторизации до итоговой суммы в корзине.")
@allure.severity(allure.severity_level.BLOCKER)
def test_shop_purchase(driver: WebDriver) -> None:
    """Сквозной тест покупки товаров в магазине."""

    # Все шаги внутри методов уже помечены @allure.step
    auth_page = AuthPage(driver)
    auth_page.login_and_password()

    inventory_page = InventoryPage(driver)
    inventory_page.add_items()

    cart_page = CartPage(driver)
    cart_page.click_checkout()

    form_page = CheckoutFormPage(driver)
    form_page.fill_in()

    summary_page = CheckoutSummaryPage(driver)

    with allure.step("Проверить итоговую сумму заказа"):
        price_total_text = summary_page.get_total_price()
        assert "$58.29" in price_total_text, (
            f"Ошибка! Ожидали $58.29, но получили: {price_total_text}"
        )
