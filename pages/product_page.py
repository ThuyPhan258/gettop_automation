from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class Product(Page):
    IMAGES = (By.CSS_SELECTOR, ".product-gallery-slider .woocommerce-product-gallery__image img")
    NAME = (By.CSS_SELECTOR, ".product-title.product_title.entry-title")
    PRICE = (By.CSS_SELECTOR, "p[class='price product-page-price price-on-sale'] ins span[class='woocommerce-Price-amount amount']")
    DESCRIPTION = (By.CSS_SELECTOR, ".product-short-description")
    HOME_LINK = (By.CSS_SELECTOR, "a[href='https://gettop.us']")
    CATEGORY_LINK = (By.CSS_SELECTOR, ".posted_in a")
    FB_ICON = (By.CSS_SELECTOR, ".share-icons .icon-facebook")
    TWITTER_ICON = (By.CSS_SELECTOR, ".share-icons .icon-twitter")
    EMAIL_ICON = (By.CSS_SELECTOR, ".share-icons .icon-envelop")
    PINTEREST_ICON = (By.CSS_SELECTOR, ".share-icons .icon-pinterest")
    TUMBLR_ICON = (By.CSS_SELECTOR, ".share-icons .icon-tumblr")

    def verify_image_product(self):
        images = self.find_elements(*self.IMAGES)
        assert (len(images) != 0),f'Error Element not present'

    def verify_name_product(self):
        name = self.find_elements(*self.NAME)
        assert (len(name) != 0),f'Error Element not present'

    def verify_price_product(self):
        price = self.find_elements(*self.PRICE)
        assert (len(price) != 0),f'Error Element not present'

    def verify_description_product(self):
        description = self.find_elements(*self.PRICE)
        assert (len(description) != 0),f'Error Element not present'

    def hover_link(self, link):
        category = self.find_element(*link)
        actions = ActionChains(self.driver)
        actions.move_to_element(category)
        actions.perform()

    def hover_home_link(self):
        self.hover_link(self.HOME_LINK)

    def hover_category_link(self):
        self.hover_link(self.CATEGORY_LINK)

    def social_network_are_present(self):
        self.wait_for_element_appear(*self.FB_ICON)
        self.wait_for_element_appear(*self.TWITTER_ICON)
        self.wait_for_element_appear(*self.EMAIL_ICON)
        self.wait_for_element_appear(*self.PINTEREST_ICON)
        self.wait_for_element_appear(*self.TUMBLR_ICON)

    def hover_and_click_on_FB_icon(self):
        self.hover_link(self.FB_ICON)
        self.click(*self.FB_ICON)

    def hover_and_click_on_Twitter_icon(self):
        self.hover_link(self.TWITTER_ICON)
        self.click(*self.TWITTER_ICON)

    def hover_and_click_on_Email_icon(self):
        self.hover_link(self.EMAIL_ICON)
        self.click(*self.EMAIL_ICON)

    def hover_and_click_on_Pinterest_icon(self):
        self.hover_link(self.PINTEREST_ICON)
        self.click(*self.PINTEREST_ICON)

    def hover_and_click_on_Tumblr_icon(self):
        self.hover_link(self.TUMBLR_ICON)
        self.click(*self.TUMBLR_ICON)