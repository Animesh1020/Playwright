from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    browser = p.chromium.launch(
        headless=False
    )

    page = browser.new_page()

    page.goto(
        "https://demoqa.com/text-box"
    )

    page.locator(
        "#userName"
    ).fill("Animesh")

    page.locator(
        "#userEmail"
    ).fill("test@test.com")

    page.locator(
        "#submit"
    ).click()

    browser.close()