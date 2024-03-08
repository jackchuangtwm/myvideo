from selenium.webdriver.common.by import By
from utils.auto_tester import AutoTester
import time
from selenium.webdriver.common.by import By
import logging




class IndexPage(AutoTester):

    chrome_text_box_locator = (By.NAME, "q")


    def __init__(self, driver):
        super().__init__(driver)
    
    def key_query_text_box(self):
        logging.info('Clicking query text box')
        self.key_in(self.chrome_text_box_locator)