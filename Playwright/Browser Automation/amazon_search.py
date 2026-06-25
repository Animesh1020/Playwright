from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:

    browser = p.chromium.launch(
        headless=False
    )

    page = browser.new_page()

    page.goto(
        "https://www.amazon.in"
    )

    page.locator(
        "#twotabsearchtextbox"
    ).fill("Laptop")

    page.locator(
        "#nav-search-submit-button"
    ).click()

    expect(
        page
    ).to_have_title(
        lambda title: "Laptop" in title
    )

    browser.close()