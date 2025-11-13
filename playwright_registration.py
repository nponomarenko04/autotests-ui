from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    button_registration = page.get_by_test_id("registration-page-registration-button")
    password_input = page.get_by_test_id("registration-form-password-input").locator("input")
    username_input = page.get_by_test_id("registration-form-username-input").locator("input")
    email_input = page.get_by_test_id('registration-form-email-input').locator("input")
    dashboard_logo = page.get_by_test_id('dashboard-toolbar-title-text')

    page.goto(" https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
    email_input.fill('user.name@gmail.com')
    username_input.fill('username')
    password_input.fill('password')
    button_registration.click()
    expect(dashboard_logo).to_be_visible()
