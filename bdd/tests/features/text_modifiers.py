from lettuce import *
from modules import text_modifiers


@step('I have the string "(.*)"')
def i_have_the_string(step, string):
    world.string = string

@step('I use the uppercase function')
def i_use_the_uppercase_function(step):
    world.string = text_modifiers.uppercase(world.string)

@step('I see the string "(.*)"')
def i_see_the_string(step, expected):
    assert world.string == expected

@step('I use the lowercase function')
def i_use_the_lowercase_function(step):
    world.string = text_modifiers.lowercase(world.string)
