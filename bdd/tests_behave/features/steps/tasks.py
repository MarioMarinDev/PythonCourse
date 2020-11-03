from behave import *

@given('I am already logged in')
def step_impl(context):
    field = context.driver.find_element_by_id("email")
    field.send_keys("MarioMarin_25@outlook.com")
    field = context.driver.find_element_by_name("password")
    field.send_keys("123456789")
    btn_login = context.driver.find_element_by_xpath("//button[@type='submit']")
    btn_login.click()

@when('I click on the "{}" link')
def step_impl(context, link_text):
    btn = context.driver.find_element_by_partial_link_text(link_text)
    btn.click()

@when('I write "{}" on the "{}" field')
def step_impl(context, text, field_name):
    field = context.driver.find_element_by_name(field_name)
    field.send_keys(text)

@when('I click on the "{}" button')
def step_impl(context, button_text):
    btn = context.driver.find_element_by_xpath("//button[text()='{}']".format(button_text))
    btn.click()

@then('I see a "{}" task card')
def step_impl(context, card_title):
    card_exists = False
    cards = context.driver.find_elements_by_class_name('task-title')
    for card in cards:
        if card_title in card.text:
            card_exists = True
    assert card_exists, "No card with title: " + card_title

@when('I click on the Edit link of the "{}" task card')
def step_impl(context, task_title):
    found_card = None
    cards = context.driver.find_elements_by_class_name('task-title')
    for card in cards:
        if task_title in card.text:
            found_card = card
    root = found_card.find_element_by_xpath('..')
    root = root.find_element_by_xpath('..')
    btn_edit = root.find_element_by_partial_link_text("Edit")
    btn_edit.click()

@when('I click on the Delete button of the "{}" task card')
def step_impl(context, task_title):
    xpath = "//*[contains(@class, 'card-header') and contains(.,'{}')]".format(task_title)
    xpath += "//button[contains(.,'Delete')]"
    btn_delete = context.driver.find_element_by_xpath(xpath)
    btn_delete.click()

@then('I see a "{}" task card description')
def step_impl(context, task_description):
    assert context.driver.find_element_by_xpath("//*[text()='{}']".format(task_description))

@then('I will not see a "{}" task card')
def step_impl(context, card_title):
    card_exists = False
    cards = context.driver.find_elements_by_class_name('task-title')
    for card in cards:
        if card_title in card.text:
            card_exists = True
    assert not card_exists, "Card with title: " + card_title + " exists"











