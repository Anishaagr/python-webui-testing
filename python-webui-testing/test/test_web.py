"""
This module contains web test1 cases for the tutorial.
Tests use Selenium WebDriver with Chrome and ChromeDriver.
The fixtures set up and clean up the ChromeDriver instance.
"""

from pages.result import DuckDuckGoResultPage
from pages.search import DuckDuckGoSearchPage


def test_basic_duckduckgo_search(browser2):
    # Set up test1 case data
    PHRASE = 'panda'

    # Search for the phrase
    search_page = DuckDuckGoSearchPage(browser2)
    search_page.load()
    search_page.search(PHRASE)

    # Verify that results appear
    result_page = DuckDuckGoResultPage(browser2)
    assert result_page.link_div_count() > 0
    assert result_page.phrase_result_count(PHRASE) > 0
    assert result_page.search_input_value() == PHRASE


def test_basic(browser2):
    assert True