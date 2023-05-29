from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://develop.nutrable.com/")
    page.get_by_role("button", name="Accept All").click()
    page.get_by_role("button", name="login").click()
    page.get_by_role("button", name="Continue with Email").click()
    page.get_by_placeholder("Email").fill("piotr.franczak@cledar.pl")
    page.get_by_placeholder("Email").press("Tab")
    page.get_by_placeholder("Password").fill("Tester1234!")
    page.get_by_role("button", name="Login", exact=True).click()

    expect(page.get_by_text("I want help with...")).to_have_text('I want help with...')

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
