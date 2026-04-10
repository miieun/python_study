import pytest
from playwright.sync_api import expect
from pages.saucedemo_page import SauceDemoPage

def test_login(page):
    p = SauceDemoPage(page)
    p.open()
    p.login()
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

def test_cart(page):
    p = SauceDemoPage(page)
    p.open()
    p.login()

    p.add_to_cart(
        "sauce-labs-backpack",
        "sauce-labs-bolt-t-shirt",
        "sauce-labs-bike-light",
        "sauce-labs-fleece-jacket"
    )
    expect(p.cart_badge).to_have_text("4")

    p.cart_link.click()
    expect(page).to_have_url("https://www.saucedemo.com/cart.html")

    p.remove_from_cart("sauce-labs-backpack", "sauce-labs-bolt-t-shirt")
    expect(p.cart_badge).to_have_text("2")

    p.checkout("hong", "eeei", "17010")
    expect(page).to_have_url("https://www.saucedemo.com/checkout-complete.html")