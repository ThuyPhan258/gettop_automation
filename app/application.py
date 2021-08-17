from pages.main_page import Main
from pages.search_results_page import SearchResults
from pages.top_nav_bar_page import TopNav
from pages.sort_page import Sort
from pages.product_page import Product

class Application():

    def __init__(self, driver):
        self.driver = driver
        self.main_page = Main(self.driver)
        self.search_results_page = SearchResults(self.driver)
        self.top_nav_bar_page = TopNav(self.driver)
        self.sort_page = Sort(self.driver)
        self.product_page = Product(self.driver)