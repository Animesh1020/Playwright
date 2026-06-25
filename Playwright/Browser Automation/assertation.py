from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)

    page = browser.new_page()

    page.goto(
        "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login",
        wait_until="commit"
    )

    # Assertion 1 - Title
    expect(page).to_have_title("OrangeHRM")

    # Username
    page.get_by_placeholder("Username").fill("Admin")

    # Assertion 2 - Value
    expect(
        page.get_by_placeholder("Username")
    ).to_have_value("Admin")

    # Password
    page.get_by_placeholder("Password").fill("admin123")

    # Assertion 3 - Button Enabled
    expect(
        page.get_by_role("button", name="Login")
    ).to_be_enabled()

    # Login
    page.get_by_role("button", name="Login").click()

    # Assertion 4 - URL
    page.wait_for_url("**/dashboard/**")

    expect(page).to_have_url(
        lambda url: "dashboard" in url
    )

    # Assertion 5 - Visible
    expect(
        page.get_by_role(
            "heading",
            name="Dashboard"
        )
    ).to_be_visible()

    # Assertion 6 - Text
    expect(
        page.get_by_role(
            "heading",
            name="Dashboard"
        )
    ).to_have_text("Dashboard")

    browser.close()