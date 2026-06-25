from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.amazon.in")

time.sleep(5) 
items = driver.find_elements(
    By.XPATH,
    "(//div[@class='_Zmx1a_fluidQuadImageLabelBody_3tld0'])[2]//a//div[2]/span"
)

for item in items:
    print(item.text)

driver.quit() 