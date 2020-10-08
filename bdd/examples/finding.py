import time


def main(driver, page):
    driver.get(page)
    time.sleep(3)
    element = driver.find_element_by_id("name-id")
    element.send_keys("by id ")
    time.sleep(3)
    element = driver.find_element_by_name("name")
    element.send_keys("by name ")
    time.sleep(3)
    element = driver.find_element_by_xpath("//input[@id='name-id']")
    element.send_keys("by xpath")
    time.sleep(3)
    element = driver.find_element_by_link_text("Siguiente")
    element = driver.find_element_by_partial_link_text("Sig")
    element.click()
    time.sleep(3)
    element = driver.find_element_by_class_name("style")
    element = driver.find_element_by_css_selector(".style")
    print("Botón: " + element.text)
