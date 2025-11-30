import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage


@pytest.mark.regression
@pytest.mark.authorization
@pytest.mark.parametrize(
    "email, password",
    [
        ("user.name@gmail.com", "password"),
        ("user.name@gmail.com", ""),
        ("", "password")
    ]
)
def test_wrong_email_or_password_authorization(page: Page, email: str, password: str):
    login_page = LoginPage(page=page)
    login_page.open()  # ОТКРЫВАЕМ страницу

    # Используем временные методы
    login_page.fill_login_form(email=email, password=password)
    login_page.click_login_button()

    login_page.check_visible_wrong_email_or_password_alert()