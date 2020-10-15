from behave import fixture, use_fixture
from selenium import webdriver

@fixture
def start_chrome_driver(context):
    context.driver = webdriver.Chrome(executable_path="drivers/chromedriver.exe")

# before_all
def before_feature(context, feature):
    use_fixture(start_chrome_driver, context)

def after_feature(context, feature):
    context.driver.close()