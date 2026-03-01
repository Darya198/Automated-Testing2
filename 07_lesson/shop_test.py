import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager

from shop_1page import MainPage
from shop_2page import SearchPage
from shop_3page import CartPage
from shop_4page import FormPage
from shop_5page import LastPage


@pytest.fixture
def driver():
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


def test_calc(driver: WebDriver):
    page = MainPage(driver)
    page.login_and_password()

    page = SearchPage(driver)
    page.add_items()

    page = CartPage(driver)
    page.click_checkout()

    page = FormPage(driver)
    page.fill_in()

    page = LastPage(driver)
    price_total_text = page.price()

    assert "$58.29" in price_total_text, f"Ошибка! Получено: {
        price_total_text}"
