import os

import pytest

from LoginPageObjects import LoginPage
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class Test_001_login:

   def test_login(self):
       self.driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
       self.lp=LoginPage(self.driver)
       self.lp.setUserName("admin@yourstore.com")
       self.lp.setPassword("admin")
       self.lp.clickLogin()
       act_title=self.driver.title

       screenshot_path = os.path.join(os.getcwd(), "Screenshots", "test_login.png")

       if act_title == "Dashboard / nopCommerce administration":
           assert True
           self.driver.close()

       else:

           assert False
           self.driver.close()
