import pytest
from pages.registration_page import RegistrationPage
from pages.dashboard_page import DashboardPage

@pytest.fixture(scope="function")
def registration_page(page):
    return RegistrationPage(page)

@pytest.fixture(scope="function")
def dashboard_page(page):
    return DashboardPage(page)