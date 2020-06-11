import pytest
from pages.result import WikiArticlePage
from pages.search import WikiSearchPage

def test_basic_search(browser):
    PHRASE = 'schipperke'

    search_page = WikiSearchPage(browser)
    search_page.load_page()
    search_page.search(PHRASE)
    result_page = WikiArticlePage(browser)
    assert result_page.get_img('Schipperke0001.jpg') == 1

