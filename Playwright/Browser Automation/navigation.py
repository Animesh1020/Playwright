from playwright.sync_api import sync_playwright, expect
import re

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)

    page = browser.new_page()

    # Open OrangeHRM
    page.goto(
        "https://opensource-demo.orangehrmlive.com/"
    )

    # Login
    page.get_by_placeholder(
        "Username"
    ).fill("Admin")

    page.get_by_placeholder(
        "Password"
    ).fill("admin123")

    page.get_by_role(
        "button",
        name="Login"
    ).click()

    # Wait for navigation to Dashboard
    page.wait_for_url(
        "**/dashboard/**"
    )

    # Verify URL using Regex
    expect(page).to_have_url(
        re.compile(r".*dashboard.*")
    )

    # Verify Dashboard heading
    expect(
        page.get_by_role(
            "heading",
            name="Dashboard"
        )
    ).to_be_visible()

    print("Login Successful and Dashboard Loaded")

    browser.close()