import time

import pytest
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager import *
from selenium.webdriver.chrome.service import Service
from selenium import webdriver

class TestLogin:
    def test_login_chrome(self):
        driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        time.sleep(10)
        driver.get("https://ranheim-test.imoee.apteancloud.com/oee")

    def test_login_edge(self):
        driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
        time.sleep(10)
        driver.get("https://ranheim-test.imoee.apteancloud.com/oee")
    def test_login_firefox(self):
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        time.sleep(10)
        driver.get("https://ranheim-test.imoee.apteancloud.com/oee")