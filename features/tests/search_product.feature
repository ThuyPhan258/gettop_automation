Feature: Test search product functionality

  Scenario: User can search for existing product and sees correct results
    Given Open Gettop page
    When Hover on search icon
    When Input Macbook in search field
    And Click Enter
    Then Verify search worked

  Scenario: User can see number of search results
    Given Open Gettop page
    When Hover on search icon
    When Input Macbook in search field
    Then Verify list of search suggestion

  Scenario: User can search for non-existing product and see "No products found"
    Given Open Gettop page
    When Hover on search icon
    When Input Coke in search field
    And Click Enter
    Then Verify the text "No products found" displays in product page

