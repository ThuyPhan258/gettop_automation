from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

SEARCH_ICON =(By.CSS_SELECTOR, "#header .header-search-form button.ux-search-submit")

@given('Open Gettop page')
def open_Gettop_page(context):
    context.app.main_page.open_main()

@when('Hover on search icon')
def hover_search_icon(context):
    context.app.search_results_page.hover_search_icon()

@when('Input {search_word} in search field')
def input_text_search(context, search_word):
    context.app.search_results_page.input_search(search_word)

@when("Click Enter")
def click_Enter(context):
    context.app.search_results_page.verify_search_icon_present()
    context.driver.find_element(*SEARCH_ICON).click()

@then('Verify search worked')
def verify_search_work(context):
    sleep(3)
    expected_text = "HOME / SHOP / SEARCH RESULTS FOR “MACBOOK”"
    actual_text = context.driver.find_element(By.CSS_SELECTOR, "#wrapper .shop-page-title .woocommerce-breadcrumb").text.upper()
    assert actual_text == expected_text, f'Error {actual_text}, but expected {expected_text}'

@then('Verify list of search suggestion')
def verify_number_search_result(context):
    context.driver.implicitly_wait(5)
    search_list = context.driver.find_elements(By.CSS_SELECTOR, ".header-search .autocomplete-suggestions div.autocomplete-suggestion .search-name strong")

    print("Total suggestion search list are:", len(search_list))

    for ele in search_list:
        print(ele.text)

@then('Verify the text "No products found" displays in product page')
def verify_no_existing_product_search(context):
    sleep(3)
    expected_result = "No products were found matching your selection."
    actual_result = context.driver.find_element(By.CSS_SELECTOR, ".shop-container .woocommerce-info").text
    assert actual_result == expected_result, f'Error {actual_result}, but expected {expected_result}'

