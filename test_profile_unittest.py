import unittest
from selenium import webdriver

class TestProfile(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
    
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
    def test_open_profile(self):
        self.driver.get("https://example.com/profile")
        self.assertIn("Profile", self.driver.title)
