from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

driver.maximize_window()

driver.get('http://the-internet.herokuapp.com/login')

username = 'input[type="text"]'
search_box1 = driver.find_element(By.CSS_SELECTOR, username)
search_box1.send_keys('tomsmith')

password = 'input[type="password"]'
search_box2 = driver.find_element(By.CSS_SELECTOR, password)
search_box2.send_keys('SuperSecretPassword!')

button_selector = 'button.radius'
driver.find_element(By.CSS_SELECTOR, button_selector).click()

flash_message = driver.find_element(By.CSS_SELECTOR, '.flash.success')
print(flash_message.text)

driver.quit()
