# Created by huy at 8/9/21
Feature: Test filter product price functionality

  Scenario: User can filter products by drag and drop
    Given Opens a product sorting page
    When Drag minimum product price
    When Drag maximum product price
    When Click Filter button
    Then Verify list of products

  Scenario: User can reset price filter after it was applied by tapping on closing X from Applied Filters
    Given Opens a product sorting page
    When Drag minimum product price
    When Drag maximum product price
    When Click Filter button
    When Click Reset Min and Max Filter
    Then Verify list of products
