'''from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://opensource-demo.orangehrmlive.com/")

    page.get_by_placeholder("Username").fill("Admin")
    page.get_by_placeholder("Password").fill("admin123")
    page.get_by_role("button", name="Login").click()

    page.locator(".oxd-userdropdown-tab").click()
    page.get_by_text("Logout").click()

    expect(page.get_by_placeholder("Username")).to_be_visible()

    print("Logout Successful")

    browser.close()'''
    
    
#Trace_Viewer

from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)

    # Create context
    context = browser.new_context()

    # Start tracing
    context.tracing.start(
        screenshots=True,
        snapshots=True,
        sources=True
    )

    page = context.new_page()

    page.goto("https://opensource-demo.orangehrmlive.com/")

    page.get_by_placeholder("Username").fill("Admin")
    page.get_by_placeholder("Password").fill("admin123")
    page.get_by_role("button", name="Login").click()

    page.locator(".oxd-userdropdown-tab").click()
    page.get_by_text("Logout").click()

    expect(page.get_by_placeholder("Username")).to_be_visible()

    print("Logout Successful")

    # Stop tracing and save file
    context.tracing.stop(path="logout_trace.zip")

    browser.close()