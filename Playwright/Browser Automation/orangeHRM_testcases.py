# from playwright.sync_api import sync_playwright, expect

# with sync_playwright() as p:

#     browser = p.chromium.launch(headless=False)
#     page = browser.new_page()

#     page.goto("https://opensource-demo.orangehrmlive.com/")

#     page.get_by_placeholder("Username").fill("Admin")
#     page.get_by_placeholder("Password").fill("admin123")

#     page.get_by_role("button", name="Login").click()

#     # Verify Dashboard Heading
#     expect(
#         page.get_by_role("heading", name="Dashboard")
#     ).to_be_visible()

#     print("Login Successful")

#     browser.close()
    
#Invalid Password

from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)

    page = browser.new_page()

    page.goto(
        "https://opensource-demo.orangehrmlive.com/"
    )

    page.get_by_placeholder(
        "Username"
    ).fill("Admin")

    page.get_by_placeholder(
        "Password"
    ).fill("wrong123")
    
    page.get_by_role(
        "button",
        name="Login"
    ).click()

    expect(
        page.get_by_text(
            "Invalid credentials"
        )
    ).to_be_visible()

    browser.close()