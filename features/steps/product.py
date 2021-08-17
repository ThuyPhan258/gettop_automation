import time

from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

@given('Open a {product_name} page')
def open_product_page(context, product_name):
    product_url = product_name.lower().replace(" ", '-')
    context.driver.get(f'https://gettop.us/product/{product_url}/')

@then('Verify {product_name} has image')
def verify_image_product(context, product_name):
    time.sleep(2)
    context.app.product_page.verify_image_product()

@then('Verify {product_name} has name')
def verify_name_product(context, product_name):
    time.sleep(2)
    context.app.product_page.verify_name_product()

@when('Click image to view enlarge mode')
def view_enlarge_mode(context):
    images = context.driver.find_elements(By.CSS_SELECTOR, ".product-gallery-slider .woocommerce-product-gallery__image img")
    images[0].click()

@when('Hover on heart icon')
def hover_on_heart_icon(context):
    heart_icon = context.driver.find_element(By.XPATH, "//i[@class='icon-heart']")
    actions = ActionChains(context.driver)
    actions.move_to_element(heart_icon)
    actions.perform()

@when('Click on heart icon')
def click_on_heart_icon(context):
    context.driver.find_element(By.XPATH, "//i[@class='icon-heart']").click()
    sleep(5)

@when('Store original window')
def store_window(context):
    context.original_window = context.driver.current_window_handle

@when('Hover on {link_text} link')
def hover_home_link(context, link_text):
    context.app.product_page.hover_home_link()

@when('Click on {link_text} link')
def click_home_link(context, link_text):
    link = context.driver.find_element(By.XPATH, "//nav[contains(@class,'woocommerce-breadcrumb')]//a[normalize-space()='" + link_text + "']")
    link.click()

@when('Hover and click on Facebook icon')
def hover_and_click_on_FB_icon(context):
    context.app.product_page.hover_and_click_on_FB_icon()

@when('Hover and click on Twitter icon')
def hover_and_click_on_Tw_icon(context):
    context.app.product_page.hover_and_click_on_Twitter_icon()

@when('Switch to new window')
def switch_window(context):
    context.driver.wait.until(EC.new_window_is_opened)

    new_window = context.driver.window_handles[1]
    context.driver.switch_to_window(new_window)

@then('Verify {social_network_name} link opens a new window to login to social network')
def verify_social_network_url_opens(context, social_network_name):
    assert social_network_name in context.driver.current_url, \
        f'{social_network_name} not in {context.driver.current_url}'

@then('Verify Home page window url opens')
def Home_page_windown_opens(context):
    assert 'https://gettop.us/' in context.driver.current_url,\
        f'URL https://gettop.us/ not in {context.driver.current_url}'

@then('Verify {category_name} in category page window url opens')
def Category_page_windown_opens(context, category_name):
    assert category_name in context.driver.current_url,\
        f'{category_name} not in {context.driver.current_url}'

@then('Verify product has been added to wishlist')
def verify_product_added_to_wishlist(context):

    actual_text = context.driver.find_element(By.CSS_SELECTOR, ".wishlist-popup").text
    print(actual_text)
    expected_text = "Browse wishlist"
    assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'

@then('Verify {product_name} has price')
def verify_price_product(context, product_name):
    time.sleep(2)
    context.app.product_page.verify_price_product()

@then('Verify {product_name} has description')
def verify_description_product(context, product_name):
    time.sleep(2)
    context.app.product_page.verify_description_product()

@then('Verify zoomin and zoomout product image')
def zoom_image(context):
    timeout = 10
    #zoom in by 200%
    context.driver.execute_script('document.body.style.MozTransform = "scale(2.0)";')
    context.driver.execute_script('document.body.style.MozTransformOrigin = "0 0";')
    sleep(5)

    #zoon out by 100%
    context.driver.execute_script('document.body.style.zoom = "scale(1.0)";')
    context.driver.execute_script('document.body.style.MozTransformOrigin = "0 0";')
    sleep(5)

@then('Verify scroll thru images and close them')
def scroll_thru_images(context):
    next_arrow = context.driver.find_element(By.XPATH, "//button[@aria-label='Next (arrow right)']")
    back_arrow = context.driver.find_element(By.XPATH, "//button[@aria-label='Previous (arrow left)']")
    images = context.driver.find_elements(By.CSS_SELECTOR, ".product-main .flickity-slider .col")
    for image in images:
        next_arrow.click()
        sleep(3)
        back_arrow.click()

@then('Verify closing image by clicking x')
def closing_image(context):
    context.driver.find_element(By.XPATH, "//button[@aria-label='Close (Esc)']").click()

@then('Verify Social network logos are present: FB, Twitter, Email, Pinterest LinkedIn')
def social_network_displays(context):
    context.app.product_page.social_network_are_present()
