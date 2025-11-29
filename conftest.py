import pytest
from playwright.sync_api import Playwright, Page, expect
from pages.registration_page import RegistrationPage
from pages.dashboard_page import DashboardPage
from pages.courses_list_page import CoursesListPage
from pages.create_course_page import CreateCoursePage


@pytest.fixture(scope="session")
def initialize_browser_state(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(
        storage_state="browser-state.json",
        viewport={'width': 1920, 'height': 1080}  # Добавьте эту строку
    )
    page = context.new_page()


    button_registration = page.get_by_test_id("registration-page-registration-button")
    password_input = page.get_by_test_id("registration-form-password-input").locator("input")
    username_input = page.get_by_test_id("registration-form-username-input").locator("input")
    email_input = page.get_by_test_id('registration-form-email-input').locator("input")

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    email_input.fill('user.name@gmail.com')
    username_input.fill('username')
    password_input.fill('password')
    button_registration.click()

    expect(page.locator('[data-testid="navigation-navbar-app-title-text"]')).to_be_visible()

    context.storage_state(path='browser-state.json')
    browser.close()


@pytest.fixture(scope="function")
def chromium_page_with_state(initialize_browser_state, playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(
        storage_state="browser-state.json",
        viewport={'width': 1920, 'height': 1080}  # Добавьте эту строку
    )

    page = context.new_page()

    yield page
    browser.close()


@pytest.fixture(scope="function")
def registration_page(page):
    return RegistrationPage(page)


@pytest.fixture(scope="function")
def dashboard_page(auth_page):
    return DashboardPage(auth_page)


@pytest.fixture(scope="function")
def courses_list_page(auth_page):
    return CoursesListPage(auth_page)


@pytest.fixture(scope="function")
def create_course_page(auth_page):
    return CreateCoursePage(auth_page)

