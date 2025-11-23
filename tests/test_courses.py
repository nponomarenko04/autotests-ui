from playwright.sync_api import sync_playwright, expect,Page
import pytest

@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state: Page):
    page = chromium_page_with_state
    empty_courses_icon = page.get_by_test_id('courses-list-empty-view-icon')
    empty_courses_list = page.get_by_test_id('courses-list-empty-view-title-text')
    empty_courses_text = page.get_by_test_id('courses-list-empty-view-description-text')
    courses_logo = page.get_by_test_id('courses-list-toolbar-title-text')

    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')
    expect(courses_logo).to_be_visible()
    expect(empty_courses_icon).to_be_visible()
    expect(empty_courses_list).to_have_text("There is no results")
    expect(empty_courses_text).to_have_text("Results from the load test pipeline will be displayed here")
