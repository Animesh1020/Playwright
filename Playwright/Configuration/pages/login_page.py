from playwright.sync_api import expect


class LoginPage:

    def __init__(self, page):

        self.page = page

    def navigate(self):

        self.page.goto(
            "https://opensource-demo.orangehrmlive.com/"
        )

    def login(self, username, password):

        self.page.get_by_placeholder(
            "Username"
        ).fill(username)

        self.page.get_by_placeholder(
            "Password"
        ).fill(password)

        self.page.get_by_role(
            "button",
            name="Login"
        ).click()

    def verify_dashboard(self):

        expect(
            self.page.get_by_role(
                "heading",
                name="Dashboard"
            )
        ).to_be_visible()

    def verify_invalid_credentials(self):

        expect(
            self.page.get_by_text(
                "Invalid credentials"
            )
        ).to_be_visible()

    def verify_required_message(self):

        expect(
            self.page.get_by_text(
                "Required"
            ).first
        ).to_be_visible()