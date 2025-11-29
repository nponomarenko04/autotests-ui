from playwright.sync_api import Page, expect
from components.base_component import BaseComponent


class SidebarComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.sidebar_dashboard_button = page.get_by_test_id('dashboard-drawer-list-item-button')
        self.sidebar_courses_button = page.get_by_test_id('courses-drawer-list-item-button')
        self.sidebar_logout_button = page.get_by_test_id('logout-drawer-list-item-button')

    def check_visible_sidebar(self):
        expect(self.sidebar_dashboard_button).to_be_visible()
        expect(self.sidebar_dashboard_button).to_have_text('Dashboard')

        expect(self.sidebar_courses_button).to_be_visible()
        expect(self.sidebar_courses_button).to_have_text('Courses')

        expect(self.sidebar_logout_button).to_be_visible()
        expect(self.sidebar_logout_button).to_have_text('Logout')