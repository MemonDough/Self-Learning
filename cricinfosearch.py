import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class TestCricinfoSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("C:/Program Files (x86)/chromedriver.exe")
        self.driver.maximize_window()
        

    def test_search_virat_kohli(self):
        self.driver.get("https://www.espncricinfo.com")
        time.sleep(20)
        cancelupdate = self.driver.find_element(By.ID,"wzrk-cancel")
        cancelupdate.click()
        time.sleep(2)
        search_box = self.driver.find_element(By.CSS_SELECTOR, ".icon-search-outlined.ds-text-icon-inverse.ci-nav-item.ci-nav-hover")
        search_box.click()
        time.sleep(3)
        searchbar = self.driver.find_element(By.CSS_SELECTOR,"input[placeholder='Search Players, Teams or Series']")
        time.sleep(1)
        searchbar.send_keys("Virat Kohli")
        searchbar.submit()
        time.sleep(5)
        self.assertIn("Kohli",self.driver.title)

        time.sleep(5)

        
      


    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
