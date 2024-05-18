from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open Target main page')
def open_target(context):
    context.driver.get('https://www.target.com/')

@when("Click on 'cart icon'")
def click_cart_icon(context):
    context.driver.find_element(By.XPATH, "//*[@data-test='@web/CartIcon']").click()
    sleep(3)

@then("Verify 'Your cart is empty' message displayed")
def verify_message_displayed(context):
    actual_text = context.driver.find_element(By.XPATH,"//*[@data-test='boxEmptyMsg']").text
    assert 'Your cart is empty' in actual_text, f'Error! Text Your cart is empty not in {actual_text}'
    sleep(3)


@when("Click on 'Sign In'")
def click_sign_in(context):
    context.driver.find_element(By.XPATH, "//*[@data-test='@web/AccountLink']").click()
    sleep(3)
@when("Click on 'Sign In' from right")
def click_sign_in_right(context):
    context.driver.find_element(By.XPATH, "//*[@data-test='accountNav-signIn']").click()
    sleep(3)
@then('Verify Sign In form opens')
def verify_sign_in_form(context):
    actual_text = context.driver.find_element(By.CSS_SELECTOR, "h1[class*='styles__StyledHeading-sc-1xmf98v-0 styles__AuthHeading-sc-kz6dq2-2 jhKFiw kcHdEa']").text
    assert "Sign in' in actual_text, f'Error! Text 'Sign in'  not in {actual_text}"





