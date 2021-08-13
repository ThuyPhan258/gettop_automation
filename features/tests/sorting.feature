# Created by huy at 8/11/21
Feature: Test sorting product by latest

  Scenario: User can sort products by Latest
    Given Open products page
    When Click Sort By Latest
    Then Verify query orderby=date will appear in page URL

  Scenario: User can go through all product pages after they sorted by Latest
    Given Open products page
    When Click Sort By Latest
    When Scroll down the bottom of page
    Then Verify that user can go through all product pages after sorted by Latest

  Scenario: After user sorts products by Latest, they can then reset to Default Sorting
    Given Open products page
    When Click Sort By Latest
    When Click sort by default
    Then Verify query orderby=menu_order will appear in page URL

  Scenario: When user changes Default Sorting to Sort by price: low to high, products are displayed in correct order
    Given Open products page
    When Click Sort By Price: Low to High
    Then Verify products are displayed in correct order asc

  Scenario: When user changes Default Sorting to Sort by price: high to low, products are displayed in correct order
    Given Open products page
    When Click Sort By Price: High to Low
    Then Verify products are displayed in correct order dsc

  Scenario: user opens https://gettop.us/shop/?orderby=price-desc directly, products are displayed in correct order, Sort by price: high to low option is preselected
    Given Open products page by sorting dsc
    Then Verify products are displayed in correct order dsc
    And Verify Sort by price: high to low is presented

  Scenario: user opens https://gettop.us/shop/?orderby=price directly, products are displayed in correct order, Sort by price: low to high option is preselected
    Given Open products page by sorting asc
    Then Verify products are displayed in correct order asc
    And Verify Sort by price: low to high is presented