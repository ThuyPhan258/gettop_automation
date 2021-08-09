# Created by huy at 8/5/21
Feature: Test product category functionality

  Scenario: User can hover over Mac and see correct menu options
    Given Open Gettop page
    When Hover on Mac product category
    Then See correct Mac menu options

  Scenario: User can hover over Iphone and see correct menu options
    Given Open Gettop page
    When Hover on Iphone product category
    Then See correct Iphone menu options

  Scenario: User can hover over Ipad and see correct menu options
    Given Open Gettop page
    When Hover on Ipad product category
    Then See correct Ipad menu options

  Scenario: User can hover over Watch and see correct menu options
    Given Open Gettop page
    When Hover on Watch product category
    Then See correct Watch menu options

  Scenario: User can hover over Accessories and see correct menu options
    Given Open Gettop page
    When Hover on Accessories product category
    Then See correct Accessories menu options

  Scenario: User can select Mac product from top menu and correct page opens
    Given Open Gettop page
    When Hover on Mac product category
    When Select the first product
    Then See correct MacBook Pro 13-inch page open


