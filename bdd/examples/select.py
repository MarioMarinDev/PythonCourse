from time import sleep
from selenium.webdriver.support.ui import Select


def main(driver, page):
    driver.get(page)
    all_options = driver.find_elements_by_tag_name("option")
    for option in all_options:
        print("Value is: " + option.get_attribute("value"))
        option.click()
        sleep(1)
    options = Select(driver.find_element_by_id("options"))
    options.select_by_index(0)
    sleep(3)
    options.select_by_visible_text("Opción 3")
    sleep(3)
    options.select_by_value("5")
    sleep(3)
