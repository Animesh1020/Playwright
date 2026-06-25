from pages.login_page import LoginPage


def test_valid_login(page):

    login_page = LoginPage(page)

    login_page.navigate()

    login_page.login(
        "Admin",
        "admin123"
    )

    login_page.verify_dashboard()


def test_invalid_username(page):

    login_page = LoginPage(page)

    login_page.navigate()

    login_page.login(
        "WrongUser",
        "admin123"
    )

    login_page.verify_invalid_credentials()


def test_invalid_password(page):

    login_page = LoginPage(page)

    login_page.navigate()

    login_page.login(
        "Admin",
        "wrongpass"
    )

    login_page.verify_invalid_credentials()


def test_blank_username(page):

    login_page = LoginPage(page)

    login_page.navigate()

    login_page.login(
        "",
        "admin123"
    )

    login_page.verify_required_message()


def test_blank_password(page):

    login_page = LoginPage(page)

    login_page.navigate()

    login_page.login(
        "Admin",
        ""
    )

    login_page.verify_required_message()