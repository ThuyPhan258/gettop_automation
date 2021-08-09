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

    def hover_Mac_category(self):
        mac = self.find_element(*self.MAC_CATEGORY)
        actions = ActionChains(self.driver)
        actions.move_to_element(mac)
        actions.perform()

    def hover_Iphone_category(self):
        iphone = self.find_element(*self.IPHONE_CATEGORY)
        actions = ActionChains(self.driver)
        actions.move_to_element(iphone)
        actions.perform()

    def hover_Ipad_category(self):
        ipad = self.find_element(*self.IPAD_CATEGORY)
        actions = ActionChains(self.driver)
        actions.move_to_element(ipad)
        actions.perform()

    def hover_Watch_category(self):
        watch = self.find_element(*self.WATCH_CATEGORY)
        actions = ActionChains(self.driver)
        actions.move_to_element(watch)
        actions.perform()

    def hover_Accesories_category(self):
        accessories = self.find_element(*self.ACCESSORIES_CATEGORY)
        actions = ActionChains(self.driver)
        actions.move_to_element(accessories)
        actions.perform()

    def select_first_product(self):
        e = self.find_elements(*self.PRODUCT_OPTIONS)
        e[0].click()

    def open_correct_product_page(self, expected_title: str):
        self.verify_text(expected_title, *self.PRODUCT_TITLE)