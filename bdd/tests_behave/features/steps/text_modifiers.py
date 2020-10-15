from behave import *
from modules.text_modifiers import uppercase
from modules.text_modifiers import lowercase
from modules.text_modifiers import only_numbers


@given('I have the string "{text}"')
def step_impl(context, text):
    context.string = text

@when('I use the uppercase function')
def step_impl(context):
    context.string = uppercase(context.string)

@when('I use the lowercase function')
def step_impl(context):
    context.string = lowercase(context.string)

@when('I use the only numbers function')
def step_impl(context):
    context.string = only_numbers(context.string)

@then('I see the string "{expected}"')
def step_impl(context, expected):
    assert context.string == expected, context.string + " | " + expected

@then('I see the string ""')
def step_impl(context):
    assert context.string == ""