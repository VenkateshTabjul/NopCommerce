from selenium import webdriver
import pytest


@pytest.fixture()  # keeping common lines in one conftest.py to avoid duplication
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("Launching Chrome Browser ............")
    elif browser == 'firefox':
        driver = webdriver.Firefox(executable_path="K:\VenkateshTabjul\Selenium\Drivers\geckodriver.exe")
        print("Launching Firefox Browser ............")
    else:
        driver = webdriver.Edge(executable_path="K:\VenkateshTabjul\Selenium\Drivers\msedgedriver.exe")
        print("Launching Edge Browser ............")
    return driver

def pytest_addoption(parser):     # This will get the value from hooks/cmd prompt
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):      # This will return the Browser value to set up method
    return request.config.getoption("--browser")

################# PyTest HTML Report ##################

# It is hook for adding environment info into HTML report
def pytest_configure(config):
    config._metadata['Project Name'] = 'Nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Hare Krishna'

# It is hook for delete/modify environment info into HTML report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)




