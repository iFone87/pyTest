from selenium.webdriver.common.by import By

class WikiArticlePage:

  def __init__(self, browser):
    self.browser = browser

  def get_img(self, imgAlt):
    ARTICLE_IMG = (By.CSS_SELECTOR, (f'img[alt="{imgAlt}"]'))
    imgs = self.browser.find_elements(*ARTICLE_IMG)
    if len(imgs) == 0:
      print ("Img not found on page")
    else:
      print ("Page found")
    return len(imgs)
    