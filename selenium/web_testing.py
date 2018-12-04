import unittest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class SampleTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Remote(
            command_executor='http://selenium-chrome:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.CHROME)

    # Add unit tests
    def test_nothing(self):
        driver = self.driver
        driver.get('http://web:8000/')

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
