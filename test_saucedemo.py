import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context()
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = context.new_page()
    page.goto("https://www.saucedemo.com/")
    page.locator('[data-test="username"]').click()
    page.locator('[data-test="username"]').fill("standard_user")
    page.locator('[data-test="password"]').click()
    page.locator('[data-test="password"]').fill("secret_sauce")
    page.locator('[data-test="login-button"]').click()
    page.locator('[data-test="add-to-cart-sauce-labs-backpack"]').click()
    page.locator('[data-test="shopping-cart-link"]').click()
    page.locator('[data-test="checkout"]').click()
    page.locator('[data-test="firstName"]').click()
    page.locator('[data-test="firstName"]').fill("test")
    page.locator('[data-test="lastName"]').click()
    page.locator('[data-test="lastName"]').fill("hehe")
    page.locator('[data-test="postalCode"]').click()
    page.locator('[data-test="postalCode"]').fill("123456")
    page.locator('[data-test="continue"]').click()
    page.locator('[data-test="finish"]').click()
    print("✅ Test Pass: Đã xác nhận hoàn tất đơn hàng!")
    context.tracing.stop(path="trace.zip")
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
