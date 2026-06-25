import pytest
from playwright.sync_api import sync_playwright

from config import (
    HEADLESS,
    VIEWPORT,
    TIMEOUT
)


@pytest.fixture
def page():

    with sync_playwright() as p:

        browser = p.chromium.launch(
            headless=HEADLESS
        )

        context = browser.new_context(
            viewport=VIEWPORT
        )

        page = context.new_page()

        page.set_default_timeout(
            TIMEOUT
        )

        yield page

        browser.close()