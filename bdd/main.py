from selenium import webdriver
from examples import finding
from examples import inputs
from examples import select
from examples import navigation

"""
Tres formas de usar el driver
  1. Agregar el driver al PATH
  2. Tener el driver junto al archivo que lo correrá
  3. Especificar el path al driver
"""
driver = webdriver.Chrome(executable_path="drivers/chromedriver.exe")
"""
driver.get("https://www.python.org")
element = driver.find_element_by_name("q")
element.clear()
element.send_keys("pycon")
element.send_keys(Keys.RETURN)
"""
page = "file:///C:/Users/Mario/PycharmProjects/PythonCourse/bdd/http/example.html"
finding.main(driver, page)
# inputs.main(driver, page)
# select.main(driver, page)
# navigation.main(driver, page)

driver.close()
