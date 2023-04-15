import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time

class TestCricinfoWeb(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("C:/Program Files (x86)/chromedriver.exe")
        self.driver.maximize_window()

    def test_web_one(self):
        self.driver.get("https://www.espncricinfo.com")
        self.assertIn("Cricket", self.driver.title)
        time.sleep(10)
        livebutton = self.driver.find_element(By.CSS_SELECTOR,".ci-nav-item.ci-nav-text.ci-nav-hover.ds-cursor-pointer")
        livebutton.click()
        time.sleep(5)

    
    def test_web_two(self):
        self.driver.get("https://www.espncricinfo.com/live-cricket-score")
        self.assertIn("Score", self.driver.title)
        time.sleep(25)
        clickscore = self.driver.find_element(By.CSS_SELECTOR,".ci-team-score.ds-flex.ds-justify-between.ds-items-center.ds-text-typo.ds-my-1")
        clickscore.click()
        time.sleep(5)


    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()

