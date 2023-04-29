from behave import given, when, then
from selenium import webdriver
from pages.booking_page import BookingPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


@given('Open Booking page')
def open_booking(context):
    context.app.booking_page.open_main_page()

@when('the user clicks on Sign in button')
def sign_in_button(context):
    # BookingPage(context.driver).click_sign_in_button()
    context.app.booking_page.click_sign_in_button()

@when('enters their email address "{email}" in the email address field')
def enter_email_sign_in(context, email):
    context.app.booking_page.enter_email_address(email)

@when('clicks on the Continue with email button')
def continue_email_sign_in(context):
    WebDriverWait(context.driver, 10).until(EC.visibility_of_element_located((By.ID, 'username')))
    context.app.booking_page.click_continue_with_email_button()

@when('enters their password "{password}" in the login password field')
def password_sign_in(context, password):
    context.app.booking_page.enter_password(password)

@then('clicks on the Sign in button')
def submit_sign_in(context):
    context.app.booking_page.click_sign_in_submit_button()

@then('the user should be redirected to the user account page')
def account_page_sign_in(context):
    assert context.app.booking_page.is_user_account_page_loaded()

@when('the user clicks on Register button')
def register_button(context):
    context.app.booking_page.click_register_button()

@when('the user enters their email address "{email}" in the email address field')
def emaiL_register(context, email):
    context.app.booking_page.enter_email_address_for_signup(email)

@when('clicks on the Continue with email button to register')
def continue_email_register(context):
    context.app.booking_page.click_continue_with_email_button_for_signup()

@when('enters their password "{password}" in the registration password field')
def password_register(context, password):
    context.app.booking_page.enter_password_for_signup(password)


@when('clicks on the Sign up button')
def submit_sign_up(context):
    context.app.booking_page.click_sign_up_button()

@then('the user should be redirected to their account page')
def account_page_sign_up(context):
    assert context.app.booking_page.is_account_page_loaded()




