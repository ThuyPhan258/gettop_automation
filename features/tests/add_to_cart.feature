# Created by huy at 8/4/21
Feature: Verify add to cart functionality

  Scenario: Check the number of items in the cart
    Given User opens a product page
#    When Add a product to cart
    When Click on Add to Cart button
    Then Verify cart has 1 item

  Scenario: Check the number of items after selecting quality of product to add
    Given User opens a product page
    When Add 2 products to cart
    When Click on Add to Cart button
    Then Verify cart has 2 item

  Scenario: User can type in amount of items to add to cart
    Given User opens a product page
    When Type 4 items to add to cart
    When Click on Add to Cart button
    Then Verify cart has 4 item

  Scenario: User sees " ... have been added to your cart" confirmation upon adding items to cart
    Given User opens a product page
    When Add 2 products to cart
    When Click on Add to Cart button
    Then Verify the text " ... have been added to your cart" confirmation upon adding items to cart

