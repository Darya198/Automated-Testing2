from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

driver.maximize_window()

driver.get('http://the-internet.herokuapp.com/inputs')

search_field = '[type="number"]'
search_box = driver.find_element(By.CSS_SELECTOR, search_field)

search_box.send_keys('Sky')
search_box.clear()
search_box.send_keys('Pro')

driver.quit()
