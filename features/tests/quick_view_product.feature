# Created by huy at 8/10/21
Feature: Test quick view product page

  Scenario: User can open and close Quick View by clicking on closing X
    Given Open Gettop page
    When Hover on product photo
    When Click on Quick View button
    Then Product popup opens
    When Click Close button
    Then Product popup closes

  Scenario: User can click Quick View and add product to cart
    Given Open Gettop page
    When Hover on product photo
    When Click on Quick View button
    Then Verify Add To Cart button is clickable

  Scenario: User can click multiple product pages by clicking page number
    Given Open Gettop page
    When Hover on product photo
    When Click on Quick View button
    When Click dot page 4
    Then Verify product image of page 4 displays

