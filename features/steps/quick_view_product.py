import time

from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

@when('Hover on product photo')
def hover_product(context):
    products = context.driver. find_element(By.XPATH, "//a[contains(@href,'product')]//img[@class='show-on-hover absolute fill hide-for-small back-image']")
    action = ActionChains(context.driver)
    action.move_to_element(products)
    action.perform()

@when('Click on Quick View button')
def click_Quick_View_button(context):
    context.driver.find_element(By.CSS_SELECTOR, ".quick-view.quick-view-added").click()

@then('Product popup opens')
def product_popup_opens(context):
   context.driver.wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='product-lightbox lightbox-content']")))
   time.sleep(2)

@when('Click Close button')
def click_close_button(context):
    context.driver.find_element(By.XPATH, "//button[@title='Close (Esc)']").click()


@then('Product popup closes')
def product_popup_closes(context):
    context.driver.wait.until(EC.invisibility_of_element((By.XPATH, "//div[@class='product-lightbox lightbox-content']")))

@when('Click dot page {page_number}')
def click_dot_page(context, page_number):
    dot = context.driver.find_element(By.XPATH, "//li[@aria-label='Page dot " + page_number + "']")
    print(dot)
    dot.click()
    time.sleep(2)

@then('Verify product image of page {page_number} displays')
def verify_product_image(context, page_number):
    slide = context.driver.find_element(By.XPATH, "//div[@class='product-quick-view-container']//div[@class='flickity-slider']//div[contains(@class,'slide')][" + page_number + "]")
    assert 'is-selected' in slide.get_attribute("class").split(), f'Error product image is not correct'


@then('Verify Add To Cart button is clickable')
def verify_Add_to_Cart_is_clickable(context):
    context.driver.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Add to cart']")))