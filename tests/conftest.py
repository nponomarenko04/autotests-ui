import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage
from pages.dashboard_page import DashboardPage
from pages.courses_list_page import CoursesListPage
from pages.create_course_page import CreateCoursePage

@pytest.fixture(scope="function")
def login_page(page: Page) -> LoginPage:
    return LoginPage(page)

@pytest.fixture(scope="function")
def registration_page(page: Page) -> RegistrationPage:
    return RegistrationPage(page)

@pytest.fixture(scope="function")
def dashboard_page(page: Page) -> DashboardPage:
    return DashboardPage(page)

@pytest.fixture(scope="function")
def courses_list_page(page: Page) -> CoursesListPage:
    return CoursesListPage(page)

@pytest.fixture(scope="function")
def create_course_page(page: Page) -> CreateCoursePage:
    return CreateCoursePage(page)