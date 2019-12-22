"""
This module contains DuckDuckGoSearchPage,
the page object for the DuckDuckGo search page.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

print("1st INSIDE SEARCH ")

class DuckDuckGoSearchPage:
  
    URL = 'https://www.duckduckgo.com'
    print("INSIDE SEARCH PAGE")


    SEARCH_INPUT = (By.NAME, 'q')
    #    SEARCH_INPUT = (By.ID, 'search_form_input_homepage')

    def __init__(self, browser1):
        self.browser1 = browser1

    def load(self):
        self.browser1.get(self.URL)

    def search(self, phrase):
        search_input = self.browser1.find_element(*self.SEARCH_INPUT)
        print("SEARCH KEY EXECUTED")
        search_input.send_keys(phrase + Keys.RETURN)
        print("phrase ===", phrase)

