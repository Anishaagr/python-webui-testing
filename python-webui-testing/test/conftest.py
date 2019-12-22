"""
This module contains shared fixtures for web UI test1.
"""

import json
import pytest

from selenium.webdriver import Chrome, Firefox


CONFIG_PATH = 'test/config.json'
DEFAULT_WAIT_TIME = 10
SUPPORTED_BROWSERS = ['chrome', 'firefox']


print("INSIDE CONFTEST ")
@pytest.fixture(scope='module')
def config():
    print("CONFIG FILEEEEE")
    # Read the JSON config file and returns it as a parsed dict
    with open(CONFIG_PATH) as config_file:
        data = json.load(config_file)
    return data


@pytest.fixture(scope='module')
def config_browser(config):
    print("CONFIG WEB BROWSER")
    # Validate and return the browser choice from the config data
    if 'browser' not in config:
        raise Exception('The config file does not contain "browser"')
    elif config['browser'] not in SUPPORTED_BROWSERS:
        raise Exception(f'"{config["browser"]}" is not a supported browser')
    return config['browser']


@pytest.fixture(scope='module')
def config_wait_time(config):
    print("CONFIG WAIT TIME")
    # Validate and return the wait time from the config data
    return config['wait_time'] if 'wait_time' in config else DEFAULT_WAIT_TIME


@pytest.fixture(scope='module')
def browser2(config_browser, config_wait_time):
    print("BROWSER2=========================")
    # Initialize WebDriver
    driver = None
    if config_browser == 'chrome':
        print("CHROME DRIVER")
        driver = Chrome(executable_path="C:\\drivers\\chromedriver.exe")
    elif config_browser == 'firefox':
        driver = Firefox()
    # else:
    #     raise Exception(f'"{config_browser}" is not a supported browser')

    # Wait implicitly for elements to be ready before attempting interactions
    driver.implicitly_wait(config_wait_time)
    print("DRIVER===========", driver)

    # Return the driver object at the end of setup
    yield driver

    # For cleanup, quit the driver
    print("QUIT============", driver)
    #driver.quit()
