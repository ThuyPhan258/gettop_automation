from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class TopNav(Page):
    MAC_CATEGORY = (By.ID, "menu-item-468")
    IPHONE_CATEGORY = (By.ID, "menu-item-469")
    IPAD_CATEGORY = (By.ID, "menu-item-470")
    WATCH_CATEGORY = (By.ID, "menu-item-471")
    ACCESSORIES_CATEGORY = (By.ID, "menu-item-472")
    PRODUCT_OPTIONS = (By.CSS_SELECTOR, ".menu-item.current-dropdown ul.sub-menu li")
    PRODUCT_TITLE = (By.CSS_SELECTOR, ".product-info .product-title")


    def hover_product_category(self, product_type):
        category = self.find_element(*product_type)
        actions = ActionChains(self.driver)
        actions.move_to_element(category)
        actions.perform()

    def hover_Mac_category(self):
        self.hover_product_category(self.MAC_CATEGORY)

    def hover_Iphone_category(self):
        self.hover_product_category(self.IPHONE_CATEGORY)

    def hover_Ipad_category(self):
        self.hover_product_category(self.IPAD_CATEGORY)

    def hover_Watch_category(self):
        self.hover_product_category(self.WATCH_CATEGORY)

    def hover_Accesories_category(self):
        self.hover_product_category(self.ACCESSORIES_CATEGORY)

    def select_first_product(self):
        e = self.find_elements(*self.PRODUCT_OPTIONS)
        e[0].click()

    def open_correct_product_page(self, expected_title: str):
        self.verify_text(expected_title, *self.PRODUCT_TITLE)