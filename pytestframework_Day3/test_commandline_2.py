from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class TestCLi:
    def test_Launch(self,setup):
        self.driver = setup
        self.driver.get("https://admin-demo.nopcommerce.com/login")
        self.status=self.driver.find_element(By.XPATH,"//strong[normalize-space()='Welcome, please sign in!']").is_displayed()
        self.driver.close()
        assert self.status==True
    def test_Lgin(self,setup):
        self.driver = setup
        self.driver.get("https://admin-demo.nopcommerce.com/login")
        self.driver.find_element(By.ID, "Email").clear()
        self.driver.find_element(By.CSS_SELECTOR,"input#Email").send_keys("admin@yourstore.com")
        self.driver.find_element(By.CSS_SELECTOR,"input.password").clear()
        self.driver.find_element(By.CSS_SELECTOR,"input.password").send_keys("admin")
        # driver.find_element(By.CSS_SELECTOR,"button[type=submit]").click()
        self.driver.find_element(By.CSS_SELECTOR, "button.button-1[type=submit]").click()
        # try:
        #  self.status=print(self.driver.find_element(By.XPATH,"//h1[normalize-space()='Dashboard']").is_displayed())
        #  assert self.status==True
        # except:
        #     assert self.status==False