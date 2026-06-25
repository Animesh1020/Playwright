from pages.login_page import LoginPage


def test_valid_login(page):

    login = LoginPage(page)

    login.navigate()

    login.login(
        "Admin",
        "admin123"
    )

    login.verify_dashboard()


def test_invalid_username(page):

    login = LoginPage(page)

    login.navigate()

    login.login(
        "WrongUser",
        "admin123"
    )

    login.verify_invalid_credentials()


def test_invalid_password(page):

    login = LoginPage(page)

    login.navigate()

    login.login(
        "Admin",
        "wrongpass"
    )

    login.verify_invalid_credentials()


def test_blank_username(page):

    login = LoginPage(page)

    login.navigate()

    login.login(
        "",
        "admin123"
    )

    login.verify_required()


def test_blank_password(page):

    login = LoginPage(page)

    login.navigate()

    login.login(
        "Admin",
        ""
    )

    login.verify_required()