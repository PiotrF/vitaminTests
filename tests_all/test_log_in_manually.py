from playwright.sync_api import Playwright, sync_playwright, expect
from faker import Faker

fake = Faker()

random_email = fake.email()


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

def test_log_in_incorrect_data(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://develop.nutrable.com/")

    page.get_by_text('Accept All').click()
    page.get_by_label('login').click()
    page.get_by_text('Continue with Email').click()
    page.locator("#email").fill('piotr.franczak@cledar.pl')
    page.locator("#password").fill('IncorrectPassword')
    page.get_by_text('Login').click()

    # expect(page.query_selector('.text-danger .py-2')).to_contain_text('Invalid username or password.')
    expect(page.get_by_text("Invalid username or password.")).to_have_text('Invalid username or password.')


def test_creating_new_user(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://develop.nutrable.com/")

    page.get_by_text('Accept All').click()
    page.get_by_label('login').click()
    page.get_by_role("link", name="Create Account").click()
    page.get_by_placeholder("First Name").fill("name")
    page.get_by_placeholder("Last Name").fill("last name")
    page.get_by_placeholder("Email Address").fill(random_email)
    page.get_by_placeholder("Password", exact=True).fill("Tester1234!")
    page.get_by_placeholder("Confirm Password").fill("Tester1234!")
    page.locator("#kc-register-form path").click()
    page.get_by_role("button", name="Create Account").click()

    expect(page.get_by_role("heading", name="Confirm Your Email")).to_have_text('Confirm Your Email')
    expect(page.get_by_text("An email has been sent to you to complete your registration. Please verify your ")).to_contain_text('An email has been sent to you to complete your registration. Please verify your email address to continue.')
