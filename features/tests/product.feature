# Created by huy at 8/15/21
Feature: test product functionality

  Scenario: Product has image, name, price, description
    Given Open a iPhone SE page
    Then Verify iPhone SE has image
    And Verify iPhone SE has name
    And Verify iPhone SE has price
    And Verify iPhone SE has description

  Scenario: User can zoom in product image, scroll thru images and close them (by clicking X)
    Given Open a iPhone SE page
    When Click image to view enlarge mode
    Then Verify zoomin and zoomout product image
    And Verify scroll thru images and close them
    And Verify closing image by clicking x

  Scenario: User can add product to wishlist by hovering over product image and clicking on the heart icon
    Given Open a iPhone SE page
    When Hover on heart icon
    When Click on heart icon
    Then Verify product has been added to wishlist

  Scenario: "Home" link takes user to Home Page
    Given Open a iPhone SE page
    When Store original window
    When Hover on Home link
    When Click on Home Link
    Then Verify Home page window url opens

  Scenario: "Category" link takes user to Category Page
    Given Open a iPhone SE page
    When Hover on iPhone link
    When Click on iPhone Link
    Then Verify iphone in category page window url opens

  Scenario: Social network logos are present: FB, Twitter, Email, Pinterest LinkedIn
    Given Open a iPhone SE page
    Then Verify Social network logos are present: FB, Twitter, Email, Pinterest LinkedIn

  Scenario: Clicking on a Facebook network link opens a new window to login to social network
    Given Open a iPhone SE page
    When Store original window
    When Hover and click on Facebook icon
    When Switch to new window
    Then Verify facebook link opens a new window to login to social network

  Scenario: Clicking on a Twitter network link opens a new window to login to social network
    Given Open a iPhone SE page
    When Store original window
    When Hover and click on Twitter icon
    When Switch to new window
    Then Verify twitter link opens a new window to login to social network

