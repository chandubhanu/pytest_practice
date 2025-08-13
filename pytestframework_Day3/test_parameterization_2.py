import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class TestClass:
    @pytest.mark.parametrize('username,password',[('Admin','admin123'),('Admin','admin1234'),('Adminn','admin123')])
    def test_Lgin(self,username,password):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("https://admin-demo.nopcommerce.com/login")
        self.driver.find_element(By.ID, "Email").clear()
        self.driver.find_element(By.CSS_SELECTOR, "input#Email").send_keys(username)
        self.driver.find_element(By.CSS_SELECTOR, "input.password").clear()
        self.driver.find_element(By.CSS_SELECTOR, "input.password").send_keys(password)
        # driver.find_element(By.CSS_SELECTOR,"button[type=submit]").click()
        self.driver.find_element(By.CSS_SELECTOR, "button.button-1[type=submit]").click()
        try:
         self.status=print(self.driver.find_element(By.XPATH,"//h1[noramalize-space()='Dashboard']").is_displayed())
         assert self.status==True
        except:
            assert self.status==False