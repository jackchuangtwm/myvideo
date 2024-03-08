from ui_obj.index_page import IndexPage
import os


def test_about_us(set_driver):
    
    page_obj = IndexPage(set_driver)
    page_obj.driver.get(f'{os.getenv("UI_DOMAIN")}')
    page_obj.key_query_text_box()


