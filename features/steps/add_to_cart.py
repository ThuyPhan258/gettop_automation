from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

@given('User opens a product page')
def open_product_page(context):
    context.driver.get('https://gettop.us/product/macbook-air/')

@when('Add 2 products to cart')
def add_a_product_to_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, "input.plus.button.is-form").click()

@when('Type {product_amount} items to add to cart')
def type_amount_items_to_add(context, product_amount):
    QUANTITY = context.driver.find_element(By.CSS_SELECTOR, ".input-text.qty")
    QUANTITY.clear()
    QUANTITY.send_keys(product_amount)

@when('Click on Add to Cart button')
def click_add_to_cart(context):
    context.driver.find_element_by_name("add-to-cart").click()

@when('Remove one product out of cart')
def remove_one_product(context):
    context.driver.find_element(By.CSS_SELECTOR, "input.minus.button.is-form").click()

@then('Verify cart has {expected_count} item')
def verify_cart_count(context, expected_count):
    context.driver.implicitly_wait(15)
    # expected_count = 4
    items_count = context.driver.find_element(By.CSS_SELECTOR, ".header-nav .cart-icon").text
    print('Items in cart count:', items_count)
    assert items_count == str(expected_count), f'Expected {expected_count}, but got {items_count}'

@then('Verify the text " ... have been added to your cart" confirmation upon adding items to cart')
def verify_text_after_add_to_cart(context):
   context.driver.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.woocommerce-message .success-color .icon-checkmark')))







