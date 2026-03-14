from typing import Generator
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.remote.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from calc_page import Page_calc


@pytest.fixture
def driver() -> Generator[WebDriver, None, None]:
    """Фикстура для инициализации и закрытия драйвера Chrome."""
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])

    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    yield driver
    driver.quit()


@allure.feature("Калькулятор")
@allure.title("Проверка работы медленного калькулятора (7 + 8)")
@allure.description("Тест проверяет корректность"
                    "cложения с учетом задержки выполнения")
@allure.severity(allure.severity_level.CRITICAL)
def test_calc(driver: WebDriver) -> None:
    """Тест сложения двух чисел на странице калькулятора"""
    page = Page_calc(driver)

    # Шаги уже описаны внутри методов Page_calc через @allure.step
    page.seconds()
    page.buttons()

    with allure.step("Проверяет, что итоговый результат на экране равен 15"):
        result = driver.find_element(
            By.CSS_SELECTOR, "div.screen").text
        assert result == "15"
