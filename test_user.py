
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time
import HtmlTestRunner

class TestDemoblazeLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def take_screenshot(self, step_name):
        self.driver.save_screenshot(f"reports/{step_name}.png")

    def test_login(self):
        driver = self.driver
        driver.get("https://www.demoblaze.com/")
        driver.maximize_window()
        self.take_screenshot("homepage")

        driver.find_element(By.ID, "login2").click()
        time.sleep(2)
        driver.find_element(By.ID, "loginusername").send_keys("harsh9090")
        driver.find_element(By.ID, "loginpassword").send_keys("pass123")
        self.take_screenshot("filled_credentials")

        driver.find_element(By.XPATH, "//button[text()='Log in']").click()
        time.sleep(3)

        try:
            user_element = driver.find_element(By.ID, "nameofuser")
            print("Login Test Passed: " + user_element.text)
            self.take_screenshot("logged_in")
        except:
            print("Login Test Failed")
            self.take_screenshot("login_failed")
            self.fail("Login failed - nameofuser not found")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports'))
