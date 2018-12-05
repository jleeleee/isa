import unittest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from time import sleep

class SampleTest(unittest.TestCase):

    def setUp(self):
        sleep(5)
        self.driver = webdriver.Remote(
            command_executor='http://selenium-chrome:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.CHROME)

    def test_connect(self):
        driver = self.driver
        driver.get('http://web:8000/')
        self.assertEqual(driver.title, "partex")

    # Add unit tests
    def test_view_all_listings(self):
        driver = self.driver
        driver.get('http://web:8000/')
        self.assertEqual(driver.title, "partex")

        listings_button = self.driver.find_elements_by_xpath('//a[text()="View all listings"]')
        print(listings_button)
        listings_button[0].click()
        listings_button = self.driver.find_elements_by_xpath('//a[text()="View all listings"]')
        print(listings_button)

        self.assertEqual(driver.title, "listings")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(warnings='ignore')
