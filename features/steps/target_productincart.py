from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


SEARCH_INPUT = (By.ID, 'search')
SEARCH_ICON = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
ADD_TO_CART_ICON = (By.CSS_SELECTOR, "[id*='addToCartButton']")
SIDE_SHIPPING_ICON = (By.XPATH, "//*[@data-test='fulfillment-cell-shipping']")
SIDE_ADD_TO_CART_ICON = (By.XPATH, "//button[@data-test='shippingButton']")
CART_TOTAL = (By.CSS_SELECTOR, "[class*='CartSummarySpan']")


@given('Open Target main page')
def open_target(context):
    context.driver.get('https://www.target.com/')


@when("Search for {item}")
def search_product(context, item):
    context.driver.find_element(*SEARCH_INPUT).send_keys(item)
    context.driver.find_element(*SEARCH_ICON).click()
    sleep(6)


@when("Click add product to cart icon")
def click_add(context):
    context.wait.until(EC.element_to_be_clickable(ADD_TO_CART_ICON),
                       message='Button not clickable')
    context.driver.find_element(*ADD_TO_CART_ICON).click()


@when("Confirm add to cart icon on side navigation")
def click_shipping(context):
    context.wait.until(EC.presence_of_element_located(SIDE_SHIPPING_ICON),
                       message="Icon not present")
    context.driver.find_element(*SIDE_SHIPPING_ICON).click()


@when("Click add to cart on nav")
def click_add_on_side_nav(context):
    context.driver.find_element(*SIDE_ADD_TO_CART_ICON).click()
    context.wait.until(EC.invisibility_of_element(SIDE_ADD_TO_CART_ICON),
                       message='Side add to cart icon did not disappear')


@when("Open cart page")
def open_cart(context):
    context.driver.get("https://www.target.com/cart")


@then("Verify cart has {number} product")
def verify_cart_products(context, number):
    cart_total = context.driver.find_element(*CART_TOTAL).text
    assert number in cart_total, f"Expected {number} product received {cart_total}"
