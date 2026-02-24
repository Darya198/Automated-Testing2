import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    options = webdriver.EdgeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Edge(options=options)
    yield driver
    driver.quit()


def test_fill_form(driver):
    wait = WebDriverWait(driver, 10)
    driver.maximize_window()
    driver.get(
        'https://bonigarcia.dev/selenium-webdriver-java/data-types.html')

    form = driver.find_element(
        By.CSS_SELECTOR, "input[name='first-name']")
    form.clear()
    form.send_keys('Иван')

    form = driver.find_element(
        By.CSS_SELECTOR, "input[name='last-name']")
    form.clear()
    form.send_keys('Петров')

    form = driver.find_element(
        By.CSS_SELECTOR, "input[name='address']")
    form.clear()
    form.send_keys('Ленина, 55-3')

    form = driver.find_element(
        By.CSS_SELECTOR, "input[name='zip-code']")
    form.clear()
    form.send_keys('')

    form = driver.find_element(
        By.CSS_SELECTOR, "input[name='city']")
    form.clear()
    form.send_keys('Москва')

    form = driver.find_element(
        By.CSS_SELECTOR, "input[name='country']")
    form.clear()
    form.send_keys('Россия')

    form = driver.find_element(
        By.CSS_SELECTOR, "input[name='e-mail']")
    form.clear()
    form.send_keys('test@skypro.com')

    form = driver.find_element(
        By.CSS_SELECTOR, "input[name='phone']")
    form.clear()
    form.send_keys('+7985899998787')

    form = driver.find_element(
        By.CSS_SELECTOR, "input[name='job-position']")
    form.clear()
    form.send_keys('QA')

    form = driver.find_element(
        By.CSS_SELECTOR, "input[name='company']")
    form.clear()
    form.send_keys('SkyPro')

    driver.find_element(
        By.CSS_SELECTOR, "button[type='submit']").click()

    zip_element = wait.until(
        EC.presence_of_element_located((By.ID, "zip-code")))
    assert "alert-danger" in zip_element.get_attribute("class")

    success_fields = [
        "first-name", "last-name", "address", "city",
        "country", "e-mail", "phone", "job-position", "company"
        ]

    for field_id in success_fields:
        element = wait.until(EC.presence_of_element_located((By.ID, field_id)))
        field_class = element.get_attribute("class")
        assert "alert-success" in field_class, f"Поле {
            field_id} должно быть зеленым!"
