from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

import time

# Initialize the Chrome webdriver
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

# Open the webpage
driver.get("https://www.astica.org/vision/describe/")
time.sleep(3)
# Find the file input element using its class name
file_input = driver.find_element(By.CLASS_NAME, "custom-file-container__custom-file__custom-file-input")


# Provide the correct file path, and make sure to escape backslashes
file_path = r'C:\Users\srija\OneDrive\Desktop\osiris\img2txt\test.jpg'  # Replace with the actual file path
file_input.send_keys(file_path)
time.sleep(3)
element = driver.find_element(By.CSS_SELECTOR,".custom-file-container__image-multi-preview__single-image-process__icon")

# Click the element
element.click()



time.sleep(120)

# eye_but=driver.find_element(By.CLASS_NAME, "fas fa-eye onmlUpload_prev")
# eye_but.click()


