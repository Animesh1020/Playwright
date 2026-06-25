# from playwright.sync_api import sync_playwright
# with sync_playwright() as p:

#     browser = p.chromium.launch(headless=False)

#     page = browser.new_page()
#     page.goto("https://opensource-demo.orangehrmlive.com/")
    
#     page.get_by_placeholder("Username").fill("Admin")

#     page.get_by_placeholder("Password").fill("admin123")

#     page.get_by_role("button",name="Login").click()

#     print(page.title())

#     page.wait_for_timeout(5000)
#     browser.close()
    
    
    
from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://opensource-demo.orangehrmlive.com/")

    page.pause()

    page.get_by_placeholder("Username").fill("Admin")