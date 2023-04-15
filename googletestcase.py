import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestGoogleWebsite(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
		self.driver.maximize_window()


	def test_search(self):
		self.driver.get("https://www.google.com")
		self.assertIn("Google", self.driver.title)
		search_box = self.driver.find_element(By.NAME,"q")
		search_box.send_keys("Cricinfo")
		search_box.submit()
		self.assertIn("Cricinfo", self.driver.title)

	def tearDown(self):
		self.driver.quit()


if __name__ == "__main__":
	unittest.main()
