import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "edge":
        driver = webdriver.Edge()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Unsupported browser: {browser}")
    return driver

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata['Project Name'] = 'nopCommerce'
    metadata['Module Name'] = 'Customers'
    metadata['Tester Name'] = 'Bhanu'

    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)