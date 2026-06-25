import pytest

from pages.login_page import LoginPage


@pytest.mark.parametrize(
    "username,password,expected",
    [
        ("Admin", "admin123", "success"),

        ("WrongUser", "admin123", "failure"),

        ("Admin", "wrongpass", "failure")
    ],
    ids=[
        "Valid Login",
        "Invalid Username",
        "Invalid Password"
    ]
)
def test_login(
    page,
    username,
    password,
    expected
):

    login_page = LoginPage(page)

    login_page.navigate()

    login_page.login(
        username,
        password
    )

    if expected == "success":

        login_page.verify_dashboard()

    else:

        login_page.verify_invalid_credentials()