from behave import *

@given('I click on the login button')
def step_impl(context):
    btn_login = context.driver.find_element_by_link_text("Login")
    btn_login.click()

@when('I write "{email}" on the email field')
def step_impl(context, email):
    field = context.driver.find_element_by_id("email")
    field.send_keys(email)

@when('I write "{password}" on the password field')
def step_impl(context, password):
    field = context.driver.find_element_by_name("password")
    field.send_keys(password)

@when('I click on the login button')
def step_impl(context):
    btn_login = context.driver.find_element_by_xpath("//button[@type='submit']")
    btn_login.click()

@then('I see the Dashboard title text')
def step_impl(context):
    assert context.driver.find_element_by_id('title-dashboard')