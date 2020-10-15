from behave import *

@given('I am in the "{page}" page')
def step_impl(context, page):
    context.driver.get(page)

@when('I write "{string}" on the searchbar')
def step_impl(context, string):
    searchbar = context.driver.find_element_by_name("q")
    searchbar.send_keys(string)

@when('I click on the GO button')
def step_impl(context):
    btn_go = context.driver.find_element_by_id("submit")
    btn_go.click()

@then('I see a "{string}" message')
def step_impl(context, string):
    assert context.driver.find_element_by_xpath("//*[text()='" + string +  "']")

@when('I click on the donation link')
def step_impl(context):
    btn_donation = context.driver.find_element_by_class_name("donate-button")
    btn_donation.click()

@then('I am in the "{page}" page')
def step_impl(context, page):
    current_page = context.driver.current_url
    assert page in current_page
