import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from calc_page import Page_calc


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])

    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    yield driver
    driver.quit()


def test_calc(driver: WebDriver):
    page = Page_calc(driver)
    page.seconds()
    page.buttons()

    result = driver.find_element(
        By.CSS_SELECTOR, "div.screen").text
    assert result == "15"
