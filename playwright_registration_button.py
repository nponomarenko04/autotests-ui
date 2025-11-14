from playwright.sync_api import sync_playwright, expect

with (sync_playwright() as playwright):
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    button_registration = page.get_by_test_id("registration-page-registration-button")
    password_input = page.get_by_test_id("registration-form-password-input").locator("input")
    username_input = page.get_by_test_id("registration-form-username-input").locator("input")
    email_input = page.get_by_test_id('registration-form-email-input').locator("input")

    page.goto(" https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
    expect(button_registration).to_be_disabled()
    email_input.fill('user.name@gmail.com')
    username_input.fill('username')
    password_input.fill('password')
    expect(button_registration).to_be_enabled()
