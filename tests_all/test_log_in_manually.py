from playwright.sync_api import Playwright, sync_playwright, expect


def test_log_in_manually(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://develop.nutrable.com/")

    page.get_by_text('Accept All').click()
    page.get_by_label('login').click()
    page.get_by_text('Continue with Email').click()
    page.locator("#email").fill('piotr.franczak@cledar.pl')
    page.locator("#password").fill('Tester1234!')
    page.get_by_text('Login').click()

    expect(page.get_by_text("I want help with...")).to_have_text('I want help with...')

    # expect(page.get_by_text("I want help with...")).to_have_text('I want help with...')

    # ---------------------
    context.close()
    browser.close()



