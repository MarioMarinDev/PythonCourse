from time import sleep


def main(driver, page):
    driver.get(page)
    element = driver.find_element_by_id("button")
    sleep(3)
    element.click()
    sleep(3)
    driver.back()
    sleep(3)
    driver.forward()
    sleep(3)
