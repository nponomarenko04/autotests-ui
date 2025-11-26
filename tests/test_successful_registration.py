import pytest

@pytest.mark.registration
@pytest.mark.regression
def test_successful_registration(registration_page, dashboard_page):
    registration_page.open()
    registration_page.fill_registration_form(
        email="test@example.com",
        username="testuser",
        password="password123"
    )
    registration_page.click_registration_button()
    dashboard_page.check_dashboard_title_visible()