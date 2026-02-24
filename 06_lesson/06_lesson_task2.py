from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 10)

driver.get("http://uitestingplayground.com/textinput")

form = wait.until(EC.element_to_be_clickable(
    (By.CSS_SELECTOR, "#newButtonName")))
form.clear()
form.send_keys('SkyPro')

button = driver.find_element(By.CSS_SELECTOR, "#updatingButton")
button.click()

text = button.text

print(text)

driver.quit()
