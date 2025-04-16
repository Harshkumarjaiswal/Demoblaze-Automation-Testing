
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time
import HtmlTestRunner

class TestDemoblazeCart(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def take_screenshot(self, step_name):
        self.driver.save_screenshot(f"reports/{step_name}.png")

    def login(self, username, password):
        driver = self.driver
        driver.get("https://www.demoblaze.com/")
        driver.maximize_window()
        self.take_screenshot("homepage")
        driver.find_element(By.ID, "login2").click()
        time.sleep(2)
        driver.find_element(By.ID, "loginusername").send_keys(username)
        driver.find_element(By.ID, "loginpassword").send_keys(password)
        self.take_screenshot("credentials_entered")
        driver.find_element(By.XPATH, "//button[text()='Log in']").click()
        time.sleep(3)

    def test_add_product_to_cart(self):
        self.login("harsh9090", "pass123")
        driver = self.driver
        driver.find_element(By.LINK_TEXT, "Samsung galaxy s6").click()
        time.sleep(2)
        self.take_screenshot("product_page")

        driver.find_element(By.XPATH, "//a[text()='Add to cart']").click()
        time.sleep(2)
        try:
            alert = Alert(driver)
            alert_text = alert.text
            alert.accept()
            self.take_screenshot("alert_accepted")
            print(f"Add to Cart Test Passed: Alert - '{alert_text}'")
        except:
            self.take_screenshot("add_to_cart_failed")
            print("Add to Cart Test Failed: Alert not shown")
            self.fail("Add to Cart failed - No alert present")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports'))
