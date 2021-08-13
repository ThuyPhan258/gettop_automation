import time

from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class Sort(Page):
    SORT_OPTION = (By.XPATH, "//select[@name='orderby']")
    PAGE_NUMBER_BUTTON = (By.XPATH, "//ul[@class='page-numbers nav-pagination links text-center']")
    NEXT_PAGE_BUTTON = (By.XPATH, "//a[@class='next page-number']")
    PREVIOUS_PAGE_BUTTON = (By.XPATH, "//a[@class='prev page-number']")
    CURRENT_PAGE = (By.XPATH, "//span[@class='page-number current']")
    SHOP_URL = 'https://gettop.us/shop/?orderby=date'

    def sort_by_latest(self):
        options = self.find_element(*self.SORT_OPTION)
        drop = Select(options)

        # select by value
        drop.select_by_value('date')
        time.sleep(4)

    def sort_by_defaut(self):
        options = self.find_element(*self.SORT_OPTION)
        drop = Select(options)

        # select by value
        drop.select_by_value('menu_order')
        time.sleep(4)

    def verify_click_multiple_page_pagination(self):
        page_number_button = self.find_elements(*self.PAGE_NUMBER_BUTTON)

        for i in range(len(page_number_button)):
            page_number = page_number_button[i]
            page_number.click()
            actual_text = self.find_element(By.CSS_SELECTOR, "a[class='page-number']").text
            if i > 0:
                self.verify_url_contains_query(actual_text)

        first_page = self.find_elements(*self.PAGE_NUMBER_BUTTON)[0]
        first_page.click()
        expected_url = 'https://gettop.us/shop/?orderby=date'
        assert self.driver.current_url == expected_url, f'Expected {expected_url}, but got {self.driver.current_url}'

    def verify_click_next_page(self):
        page_number_button = self.find_elements(*self.PAGE_NUMBER_BUTTON)

        for i in range(len(page_number_button)):
            self.find_element(*self.NEXT_PAGE_BUTTON).click()
            actual_text = self.find_element(*self.CURRENT_PAGE).text
            self.verify_url_contains_query(actual_text)

    def verify_click_previous_page(self):
        page_number_button = self.find_elements(*self.PAGE_NUMBER_BUTTON)

        for i in range(len(page_number_button)):
            self.find_element(*self.PREVIOUS_PAGE_BUTTON).click()
            actual_text = self.find_element(*self.CURRENT_PAGE).text
            if actual_text not in self.driver.current_url:
                break
            self.verify_url_contains_query(actual_text)
        assert self.driver.current_url == self.SHOP_URL, f'Expected {self.SHOP_URL}, but got self.driver.current_url'

    def scroll_down(self):
        SCROLL_PAUSE_TIME = 0.5
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(SCROLL_PAUSE_TIME)







