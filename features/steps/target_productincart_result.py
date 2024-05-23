from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

CART_TOTAL = (By.CSS_SELECTOR, "[class*='CartSummarySpan']")


@then("Verify cart has {number} product")
def verify_cart_products(context, number):
    cart_total = context.driver.find_element(*CART_TOTAL).text
    assert number in cart_total, f"Expected {number} product received {cart_total}"

    #assert amount in cart_summary, f"Expected {amount} items but got {cart_summary}"