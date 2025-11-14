from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    button_registration = page.get_by_test_id("registration-page-registration-button")
    password_input = page.get_by_test_id("registration-form-password-input").locator("input")
    username_input = page.get_by_test_id("registration-form-username-input").locator("input")
    email_input = page.get_by_test_id('registration-form-email-input').locator("input")
    page.goto(" https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
    email_input.fill('user.name@gmail.com')
    username_input.fill('username')
    password_input.fill('password')
    button_registration.click()
    context.storage_state(path='browser-state.json')

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state='browser-state.json')
    page = context.new_page()
    empty_courses_icon = page.get_by_test_id('courses-list-empty-view-icon')
    empty_courses_list = page.get_by_test_id('courses-list-empty-view-title-text')
    empty_courses_text = page.get_by_test_id('courses-list-empty-view-description-text')
    courses_logo = page.get_by_test_id('courses-list-toolbar-title-text')
    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')
    expect(courses_logo).to_be_visible()
    expect(empty_courses_icon).to_be_visible()
    expect(empty_courses_list).to_have_text("There is no results")
    expect(empty_courses_text).to_have_text("Results from the load test pipeline will be displayed here")



