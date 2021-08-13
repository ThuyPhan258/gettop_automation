import time

from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

@given('Open products page')
def open_Mac_products(context):
    context.driver.get('https://gettop.us/shop/')

@given('Open products page by sorting dsc')
def open_products_page_sorted_by_dsc(context):
    context.driver.get('https://gettop.us/shop/?orderby=price-desc')

@given('Open products page by sorting asc')
def open_products_page_sorted_by_dsc(context):
    context.driver.get('https://gettop.us/shop/?orderby=price')

@when('Click Sort By Latest')
def click_sort_by_latest(context):
    context.app.sort_page.sort_by_latest()

@when('Click sort by default')
def click_sort_by_default(context):
    context.app.sort_page.sort_by_defaut()

@when('Click Sort By Price: Low to High')
def click_sort_by_price_low_to_high(context):
    context.app.sort_page.sort_by_price_low_to_high()

@when('Click Sort By Price: High to Low')
def click_sort_by_price_high_to_low(context):
    context.app.sort_page.sort_by_price_high_to_low()

@when('Scroll down the bottom of page')
def scroll_down(context):
    context.app.sort_page.scroll_down()

@then('Verify query {sorting_value} will appear in page URL')
def verify_url(context, sorting_value):
    context.app.sort_page.verify_url_contains_query(sorting_value)

@then('Verify that user can go through all product pages after sorted by Latest')
def verify_go_through_pagination(context):
    context.app.sort_page.verify_click_multiple_page_pagination()
    time.sleep(2)
    context.app.sort_page.verify_click_next_page()
    time.sleep(2)
    context.app.sort_page.verify_click_previous_page()

@then('Verify products are displayed in correct order asc')
def verify_product_display_asc_order(context):
    context.app.sort_page.display_product_after_sort_asc()

@then('Verify products are displayed in correct order dsc')
def verify_product_display_dsc_order(context):
    context.app.sort_page.display_product_after_sort_dsc()

@then('Verify {option_text} is presented')
def verify_sort_by_high_to_low_is_presented(context, option_text):
    actual = context.driver.find_element(By.CSS_SELECTOR, ".woocommerce-ordering select option[selected]").text
    assert actual == option_text, f'Expected {option_text}, but got {actual}'

