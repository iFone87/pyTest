from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class WikiSearchPage:
    
  URL = 'https://www.wikipedia.org'
  SEARCH_INPUT = (By.ID, 'searchInput')

  def __init__(self, browser):
    self.browser = browser

  def load_page(self):
    self.browser.get(self.URL)

  def search(self, phrase):
    search_input = self.browser.find_element(*self.SEARCH_INPUT)
    search_input.send_keys(phrase + Keys.RETURN)