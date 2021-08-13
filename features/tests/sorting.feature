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