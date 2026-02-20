from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

service = ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.maximize_window()

driver.get('http://uitestingplayground.com/dynamicid')

button_selector = 'button.btn.btn-primary'
driver.find_element(By.CSS_SELECTOR, button_selector).click()
