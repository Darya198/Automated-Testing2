import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])

    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    yield driver
    driver.quit()


def test_slow_calculator(driver):
    wait = WebDriverWait(driver, 50)

    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    driver.maximize_window()

    input_field = driver.find_element(By.ID, "delay")
    input_field.clear()
    input_field.send_keys("45")

    driver.find_element(By.XPATH, "//span[text()='7']").click()

    driver.find_element(By.XPATH, "//span[text()='+']").click()

    driver.find_element(By.XPATH, "//span[text()='8']").click()

    driver.find_element(By.XPATH, "//span[text()='=']").click()

    wait.until(EC.text_to_be_present_in_element((
        By.CSS_SELECTOR, ".screen"), "15"))

    result = driver.find_element(
        By.CSS_SELECTOR, ".screen").text
    assert result == "15"
