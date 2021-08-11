import time
from decimal import Decimal
from re import sub

from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

@given('Opens a product sorting page')
def open_product_sorting_page(context):
    context.driver.get('https://gettop.us/shop/?orderby=rating')

@when('Drag minimum product price')
def drag_minimum_price(context):
    min = context.driver.find_element(By.XPATH,"//div[contains(@class, 'price_slider')]/span[1]" )
    action = ActionChains(context.driver).drag_and_drop_by_offset(min, 60, 0).perform()

    # action = ActionChains(context.driver).click_and_hold(min).pause(1).move_by_offset(50, 0).release().perform()
    # action = ActionChains(context.driver).move_to_element(min).pause(1).click_and_hold(min).move_by_offset(80, 0).release().perform()
    # action = ActionChains(context.driver).drag_and_drop_by_offset(max, -80, 0).perform()
    time.sleep(2)

@when('Drag maximum product price')
def drag_maximum_price(context):
    max = context.driver.find_element(By.XPATH, "//div[contains(@class, 'price_slider')]/span[2]")
    action = ActionChains(context.driver).drag_and_drop_by_offset(max, -80, 0).perform()
    time.sleep(2)

@when('Click Filter button')
def click_filter_button(context):
    filter_button = context.driver.find_element(By.XPATH, "//button[normalize-space()='Filter']").click()

@when('Click Reset Min and Max Filter')
def reset_min_filter(context):
    min_reset = context.driver.find_element(By.XPATH, "//aside[@id='woocommerce_layered_nav_filters-10']//li[1]//a[1]").click()
    max_reset = context.driver.find_element(By.XPATH, "//aside[@id='woocommerce_layered_nav_filters-10']//li[1]//a[1]").click()
    time.sleep(2)

# @when('Click Reset Max Filter')
# def reset_max_filter(context):
#     max_reset = context.driver.find_element(By.XPATH, "//aside[@id='woocommerce_layered_nav_filters-10']//li[1]//a[1]").click()
#     time.sleep(2)

def to_money(value):
    dollar = value.replace("$", "").replace(",", "")
    print('the value is:', dollar)
    return float(dollar)


@then('Verify list of products')
def verify_product_list(context):
    # prices = context.driver.find_elements(By.CSS_SELECTOR, ".product-small:not(.sale) .product-small.box .price")
    prices = context.driver.find_elements(By.CSS_SELECTOR, ".price .woocommerce-Price-amount.amount")
    min_price_range = to_money(context.driver.find_element(By.XPATH, "//span[@class='from']").text)
    max_price_range = to_money(context.driver.find_element(By.XPATH, "//span[@class='to']").text)

    for price_element in prices:
        price = to_money(price_element.text)
        if price < min_price_range or price > max_price_range:
            print("The product out of price range")


