from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)

    context = browser.new_context()

    # Start Trace Recording
    context.tracing.start(
        screenshots=True,
        snapshots=True,
        sources=True
    )

    page = context.new_page()

    # Navigate to OrangeHRM
    page.goto("https://opensource-demo.orangehrmlive.com/")

    # Login
    page.get_by_placeholder("Username").fill("Admin")
    page.get_by_placeholder("Password").fill("admin123")

    page.get_by_role(
        "button",
        name="Login"
    ).click()

    # Wait for Dashboard URL
    page.wait_for_url("**/dashboard/**")

    # Verify Dashboard Heading
    expect(
        page.get_by_role(
            "heading",
            name="Dashboard"
        )
    ).to_be_visible()

    # Stop Trace Recording
    context.tracing.stop(
        path="trace.zip"
    )

    browser.close()