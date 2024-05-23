from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


SEARCH_INPUT = (By.ID, 'search')
SEARCH_ICON = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
ADD_TO_CART_ICON = (By.CSS_SELECTOR, "[id*='addToCartButton']")
SIDE_SHIPPING_ICON = (By.XPATH, "//*[@data-test='fulfillment-cell-shipping']")
SIDE_ADD_TO_CART_ICON = (By.XPATH, "//button[@data-test='shippingButton']")

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
    context.driver.find_element(*ADD_TO_CART_ICON).click()
    sleep(10)


@when("Confirm add to cart icon on side navigation")
def click_shipping(context):
    context.driver.find_element(*SIDE_SHIPPING_ICON).click()
    sleep(6)


@when("Click add to cart on nav")
def click_add_on_side_nav(context):
    context.driver.find_element(*SIDE_ADD_TO_CART_ICON).click()
    sleep(5)


@when("Open cart page")
def open_cart(context):
    context.driver.get("https://www.target.com/cart")
    sleep(3)