import pytest
from playwright.sync_api import Page


@pytest.mark.registration
@pytest.mark.regression
def test_successful_registration(page: Page, registration_page, dashboard_page):
    registration_page.open()

    # Заполняем форму через компонент
    registration_page.registration_form.fill(
        email="test@example.com",
        username="testuser",
        password="password123"
    )

    # Нажимаем кнопку через компонент
    registration_page.registration_form.submit_button.click()

    # Проверяем что перешли на дашборд
    dashboard_page.open()  # или проверяем текущий URL

    # Проверяем дашборд через компоненты
    dashboard_page.navbar.check_visible("testuser")
    dashboard_page.sidebar.check_visible_sidebar()
    dashboard_page.dashboard_toolbar.check_visible()