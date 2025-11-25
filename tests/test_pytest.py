import pytest
from playwright.sync_api import Page, expect

@pytest.mark.regression
@pytest.mark.authorization
@pytest.mark.parametrize(
    "email, password",
    [
        ("user.name@gmail.com", "password"),
        ("user.name@gmail.com", "  "),
        ("  ", "password")
    ]
)
def test_wrong_email_or_password_authorization(page: Page, email: str, password: str):
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
    email_input = page.locator('input[type="text"]').first
    password_input = page.locator('input[type="password"]')
    email_input.fill(email)
    password_input.fill(password)
    login_button = page.locator('button:has-text("Login")')
    login_button.click()
    error_message = page.locator('text=Wrong email or password')
    expect(error_message).to_be_visible()
    expect(error_message).to_have_text("Wrong email or password")