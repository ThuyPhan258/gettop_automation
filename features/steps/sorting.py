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

@when('Click Sort By Latest')
def click_sort_by_latest(context):
    context.app.sort_page.sort_by_latest()

@when('Click sort by default')
def click_sort_by_default(context):
    context.app.sort_page.sort_by_defaut()

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

