from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

@when('Hover on Mac product category')
def hover_Mac_category(context):
    context.app.top_nav_bar_page.hover_Mac_category()

@when('Hover on Iphone product category')
def hover_Iphone_category(context):
    context.app.top_nav_bar_page.hover_Iphone_category()

@when('Hover on Ipad product category')
def hover_Ipad_category(context):
    context.app.top_nav_bar_page.hover_Ipad_category()

@when('Hover on Watch product category')
def hover_Watch_category(context):
    context.app.top_nav_bar_page.hover_Watch_category()

@when('Hover on Accessories product category')
def hover_Accessories_category(context):
    context.app.top_nav_bar_page.hover_Accesories_category()

@when('Select the first product')
def select_first_product(context):
    context.driver.implicitly_wait(10)
    context.app.top_nav_bar_page.select_first_product()

@then('See correct Mac menu options')
def see_correct_Mac_options(context):
    context.driver.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".menu-item.current-dropdown .menu-item-object-product")))

@then('See correct Iphone menu options')
def see_correct_Iphone_options(context):
    context.driver.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".menu-item.current-dropdown ul.sub-menu li")))

@then('See correct Ipad menu options')
def see_correct_Ipad_options(context):
    context.driver.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".menu-item.current-dropdown ul.sub-menu li")))

@then('See correct Watch menu options')
def see_correct_Watch_options(context):
    context.driver.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".menu-item.current-dropdown ul.sub-menu li")))

@then('See correct Accessories menu options')
def see_correct_Accessories_options(context):
    context.driver.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".menu-item.current-dropdown ul.sub-menu li")))

@then('See correct {product_title} page open')
def see_correct_product_open(context, product_title):
    product_title = "MacBook Pro 13-inch"
    context.app.top_nav_bar_page.open_correct_product_page(product_title)