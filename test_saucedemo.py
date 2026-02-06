import re
from playwright.sync_api import Page, expect


def test_happy_case(page: Page) -> None:
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
    page.locator('[data-test="firstName"]').fill("Hong")
    page.locator('[data-test="lastName"]').click()
    page.locator('[data-test="lastName"]').fill("Trung")
    page.locator('[data-test="postalCode"]').click()
    page.locator('[data-test="postalCode"]').fill("00700")
    page.locator('[data-test="continue"]').click()
    page.locator('[data-test="finish"]').click()
    page.locator('[data-test="back-to-products"]').click()


def test_negative_case(page: Page) -> None:
    page.goto("https://www.saucedemo.com/")
    page.locator('[data-test="username"]').click()
    page.locator('[data-test="username"]').fill("locked_out_user")
    page.locator('[data-test="password"]').click()
    page.locator('[data-test="password"]').fill("secret_sauce")
    page.locator('[data-test="login-button"]').click()


def test_performance_case(page: Page) -> None:
    page.goto("https://www.saucedemo.com/")
    page.locator('[data-test="username"]').click()
    page.locator('[data-test="username"]').fill("performance_glitch_user")
    page.locator('[data-test="password"]').click()
    page.locator('[data-test="password"]').fill("secret_sauce")
    page.locator('[data-test="login-button"]').click()
    page.locator('[data-test="add-to-cart-sauce-labs-backpack"]').click()
    page.locator('[data-test="shopping-cart-link"]').click()
    page.locator('[data-test="checkout"]').click()
    page.locator('[data-test="firstName"]').click()
    page.locator('[data-test="firstName"]').fill("TEst")
    page.locator('[data-test="firstName"]').press("Tab")
    page.locator('[data-test="lastName"]').fill("Aha")
    page.locator('[data-test="postalCode"]').click()
    page.locator('[data-test="postalCode"]').fill("00700")
    page.locator('[data-test="continue"]').click()
    page.locator('[data-test="finish"]').click()
    page.locator('[data-test="back-to-products"]').click()
    page.goto("https://www.saucedemo.com/inventory-item.html?id=5")
