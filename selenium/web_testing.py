import unittest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class SampleTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Remote(
            command_executor='http://selenium-chrome:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.CHROME)

    # Add unit tests
    def test_view_all_listings(self):
        driver = self.driver
        driver.get('http://web:8000/')
        self.assertEqual(driver.title, "web")
        listings_button = driver.find_elements_by_xpath('//*[@id]')
        #print(listings_button)
        for el in listings_button:
            print(el.text)
        self.assertEqual(driver.title, "listings")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
