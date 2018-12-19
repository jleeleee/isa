import unittest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from time import sleep

class SampleTest(unittest.TestCase):

    def setUp(self):
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
        listings_button[0].click()
        title_header = self.driver.find_elements_by_xpath('//h1[text()="All listings"]')
        self.assertGreater(len(title_header), 0)

    def test_register(self):
        driver = self.driver
        driver.get("http://web:8000/register")
        first_name = driver.find_element_by_id("id_first_name")
        last_name = driver.find_element_by_id("id_last_name")
        username = driver.find_element_by_id("id_username")
        password = driver.find_element_by_id("id_password")
        email = driver.find_element_by_id("id_email")

        first_name.send_keys("Test")
        last_name.send_keys("User")
        username.send_keys("testusername2")
        password.send_keys("test")
        email.send_keys("test@example2.com\n")

        self.assertTrue(driver.current_url, "http://web:8000/")

    def test_login_and_create(self):
        driver = self.driver
        driver.get("http://web:8000/login")
        username = driver.find_element_by_id("id_username")
        password = driver.find_element_by_id("id_password")

        username.send_keys("jhoughton")
        password.send_keys("test\n")

        self.assertEqual(driver.current_url, "http://web:8000/")

        driver.get("http://web:8000/listings/create")

        self.assertFalse("login" in driver.current_url)


    def test_search(self):
        driver = self.driver
        driver.get('http://web:8000/')
        self.assertEqual(driver.title, "partex")

        search_button = self.driver.find_elements_by_xpath('//a[text()="Search"]')
        search_button[0].click()
        searchform = self.driver.find_elements_by_name('q')

        self.assertGreater(len(searchform), 0)

        searchform[0].send_keys("gtx\n")
        results = self.driver.find_elements_by_class_name("search-result")
        self.assertGreater(len(searchform), 0)

    def tearDown(self):
        self.driver.quit()

    def test_recommendation(self):
        driver = self.driver
        driver.get('http://web:8000/listings/1')
        results = self.driver.find_elements_by_class_name("recommendation")
        self.assertEqual(len(results), 2) # 1 should have 2 recommendations with default data

if __name__ == "__main__":
    sleep(5)
    unittest.main(warnings='ignore')
