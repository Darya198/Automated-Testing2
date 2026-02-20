from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get(
    'https://bonigarcia.dev/selenium-webdriver-java/loading-images.html')

wait = WebDriverWait(driver, 15)
images = wait.until(EC.visibility_of_element_located((By.XPATH, "(//img)[4]")))
images = driver.find_elements(By.TAG_NAME, "img")

if len(images) >= 3:
    image_src = images[2].get_attribute("src")
    print(f"SRC 3-й картинки: {image_src}")
else:
    print("На странице найдено меньше 3 картинок")

driver.quit()
