import time
from selenium.webdriver.common.keys import Keys


def main(driver, page):
    driver.get(page)
    element = driver.find_element_by_id("description")
    time.sleep(3)
    element.send_keys("1", Keys.RETURN, "2", Keys.RETURN, "3")
    time.sleep(3)
    element.send_keys(Keys.ARROW_UP, "2")
    time.sleep(3)