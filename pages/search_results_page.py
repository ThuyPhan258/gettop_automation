from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class SearchResults(Page):
    SEARCH_ICON =(By.CSS_SELECTOR, "i.icon-search")
    PRODUCT_RESULTS = (By.CSS_SELECTOR, "img.show-on-hover")
    SEARCH_FIELD = (By.ID, "woocommerce-product-search-field-0")

    def click_first_product(self):
        e = self.find_elements(*self.PRODUCT_RESULTS)
        e[0].click()

    def hover_search_icon(self):
        search_icon = self.find_element(*self.SEARCH_ICON)
        actions = ActionChains(self.driver)
        actions.move_to_element(search_icon)
        actions.perform()

    def input_search(self, search_word):
        self.input_text(search_word, *self.SEARCH_FIELD)

    def click_search(self):
        self.click(*self.SEARCH_ICON)

    # def verify_search_worked(self):
    #     self.verify_text('"MACBOOK"', *self.SEARCH_RESULT)

    def verify_search_icon_present(self):
        self.wait_for_element_appear(*self.SEARCH_ICON)



