from selenium import webdriver
import time

"""
def before_scenario(context, scenario):
    if "web" in scenario.tags:
        context.driver = webdriver.Chrome(executable_path="drivers/chromedriver.exe")

def after_scenario(context, scenario):
    if "web" in scenario.tags:
        context.driver.close()
"""


def before_tag(context, tag):
    if tag == "web":
        context.driver = webdriver.Chrome(executable_path="drivers/chromedriver.exe")


def after_tag(context, tag):
    if tag == "web":
        context.driver.close()


def after_step(context, step):
    time.sleep(1)
