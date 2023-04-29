from behave import given, when, then
from selenium import webdriver
from pages.search_page import SearchPage

@when('User clicks on Search Stays button')
def search_stays_button(context):
    context.app.search_page.click_search_stays_button()

@when('User enters the destination "{destination}" in the search field')
def select_destination(context, destination):
    context.app.search_page.enter_destination(destination)

@when('User selects the dates for the stay from "{checkin_date}" to "{checkout_date}"')
def select_dates(context, checkin_date, checkout_date):
    context.app.search_page.select_checkin_date(checkin_date)
    context.app.search_page.select_checkout_date(checkout_date)

@when('User clicks on Search button')
def click_search_button(context):
    context.app.search_page.click_search_button()

@then('The search results should include properties in {destination}')
def verify_search_results_include_destination(context, destination):
    context.app.search_page.is_destination_in_search_results(destination)

