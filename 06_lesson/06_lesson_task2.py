from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


service = ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("http://uitestingplayground.com/textinput")

form = driver.find_element(By.CSS_SELECTOR, "#newButtonName")
form.clear
form.send_keys('SkyPro')

button = driver.find_element(By.CSS_SELECTOR, "#updatingButton")
button.click()

txt = button.text

print(txt)

driver.quit()
