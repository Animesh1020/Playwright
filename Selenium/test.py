from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://facebook.com")

time.sleep(5)

print("URL:", driver.current_url)
print("Title:", driver.title)

input("Press Enter to continue...")

driver.find_element(
    By.XPATH,
    "//input[@id='email']"
).send_keys("animesh@gmail.com")