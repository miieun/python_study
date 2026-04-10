# pages/saucedemo_page.py

from playwright.sync_api import Page

URL = "https://www.saucedemo.com/"

class SauceDemoPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.locator("[data-test='username']")
        self.password_input = page.locator("[data-test='password']")
        self.login_button = page.locator("[data-test='login-button']")
        self.cart_badge = page.locator("[data-test='shopping-cart-badge']")
        self.cart_link = page.locator("[data-test='shopping-cart-link']")
        self.checkout_button = page.locator("[data-test='checkout']")
        self.first_name = page.locator("[data-test='firstName']")
        self.last_name = page.locator("[data-test='lastName']")
        self.postal_code = page.locator("[data-test='postalCode']")
        self.continue_button = page.locator("[data-test='continue']")
        self.finish_button = page.locator("[data-test='finish']")

    def open(self):
        self.page.goto(URL)

    def login(self, username="standard_user", password="secret_sauce"):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def add_to_cart(self, *items):
        for item in items:
            self.page.locator(f"[data-test='add-to-cart-{item}']").click()

    def remove_from_cart(self, *items):
        for item in items:
            self.page.locator(f"[data-test='remove-{item}']").click()

    def checkout(self, first, last, postal):
        self.checkout_button.click()
        self.first_name.fill(first)
        self.last_name.fill(last)
        self.postal_code.fill(postal)
        self.continue_button.click()
        self.finish_button.click()