import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class TestPythonOrg(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
        self.domain = "https://www.python.org/"

    def tearDown(self):
        self.driver.close()

    def test_search_bar(self):
        self.driver.get(self.domain)
        element = self.driver.find_element_by_name("q")
        element.send_keys("python 3")
        element.send_keys(Keys.RETURN)
        assert self.driver.find_element_by_xpath("//h2[text()='Search Python.org']")


if __name__ == '__main__':
    unittest.main()



