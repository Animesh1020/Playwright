from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

time.sleep(3)

driver.find_element(
    By.NAME,
    "username"
).send_keys("Admin")

driver.find_element(
    By.NAME,
    "password"
).send_keys("admin123")

driver.find_element(
    By.XPATH,
    "//button[@type='submit']"
).click()

time.sleep(5)

print("Login Successful")
time.sleep(5)

driver.quit()