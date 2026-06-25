from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 15)

driver.maximize_window()
driver.get("https://www.flipkart.com/account/login")

# Close popup if it appears
try:
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class,'_2KpZ6l')]"))).click()
except:
    pass

# ✅ FIXED: Target the login form input specifically
wait.until(EC.presence_of_element_located(
    (By.XPATH, "//input[@autocomplete='off' and contains(@placeholder,'Email')]")
)).send_keys("6398011877")
print("Phone entered")

# Click Request OTP
wait.until(EC.element_to_be_clickable(
    (By.XPATH, "//button[contains(text(),'Request OTP')]")
)).click()
print("OTP Requested!")

input("Press Enter to close...")
driver.quit()