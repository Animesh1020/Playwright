from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service=service)

driver.get("https://www.google.com")

print("Title:", driver.title)

print("URL:", driver.current_url)

search_box = driver.find_element(By.NAME, "q")

search_box.send_keys("Selenium Python")

print(search_box.get_attribute("name"))

driver.quit()