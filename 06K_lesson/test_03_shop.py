import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    options = webdriver.FirefoxOptions()

    service = FirefoxService(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service, options=options)

    yield driver
    driver.quit()


def test_shop(driver):
    wait = WebDriverWait(driver, 50)

    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()

    form = driver.find_element(
        By.CSS_SELECTOR, "input#user-name")
    form.clear()
    form.send_keys('standard_user')

    form = driver.find_element(
        By.CSS_SELECTOR, "input#password")
    form.clear()
    form.send_keys('secret_sauce')

    driver.find_element(By.CSS_SELECTOR,
                        "input#login-button").click()

    wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "button#add-to-cart-sauce-labs-backpack"))).click()

    wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "button#add-to-cart-sauce-labs-bolt-t-shirt")
            )).click()

    wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "button#add-to-cart-sauce-labs-onesie"))).click()

    wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, ".shopping_cart_link"))).click()

    wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "button#checkout"))).click()

    form = driver.find_element(
        By.CSS_SELECTOR, "input#first-name")
    form.clear()
    form.send_keys('Иван')

    form = driver.find_element(
        By.CSS_SELECTOR, "input#last-name")
    form.clear()
    form.send_keys('Петров')

    form = driver.find_element(
        By.CSS_SELECTOR, "input#postal-code")
    form.clear()
    form.send_keys('123456')

    wait.until(EC.element_to_be_clickable((
        By.CSS_SELECTOR, "input#continue"))).click()

    price_total_text = wait.until(
        EC.presence_of_element_located((
            By.CSS_SELECTOR, ".summary_total_label"))
    ).text

    assert "$58.29" in price_total_text, f"Ошибка! Получено: {
        price_total_text}"
