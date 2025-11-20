from playwright.sync_api import sync_playwright, expect

with (sync_playwright() as playwright):
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(" https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login",
              wait_until="networkidle"

              )
    new_text = "12345"
    page.evaluate(
        """
        (text) =>{
        const some =document.getElementById('authentication-ui-course-title-text')
        some.textContent = text
    }
        """,
        new_text
    )

    page.wait_for_timeout(5000)
