from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

SEARCH_INPUT = (By.CSS_SELECTOR, "#utilityNav-circle")
TARGET_CIRCLE = (By.CSS_SELECTOR, "#utilityNav-circle")
HEADER = (By.XPATH,"//*[@data-test='storycardWrapperElement']")
HEADER_LINKS = (By.CSS_SELECTOR, "div[class='styles__CellItemContainer-sc-3f68hg-5 uAfgQ']")


@given('Open Target main page')
def open_target(context):
    context.driver.get('https://www.target.com/')


@when("Search for {item}")
def search_icon(context, item):
    context.driver.find_element(*SEARCH_INPUT).send_keys(item)
    context.driver.find_element(*TARGET_CIRCLE).click()
    sleep(6)


@then('Verify header in shown')
def verify_header_shown(context):
    context.driver.find_element(*HEADER)


@then('Verify header has {expected_amount} links')
def verify_header_links(context, expected_amount):
    expected_amount = int(expected_amount)
    links = context.driver.find_elements(*HEADER_LINKS)
    assert len(links) == expected_amount, f'Expected {expected_amount} links but got {len(links)}'





