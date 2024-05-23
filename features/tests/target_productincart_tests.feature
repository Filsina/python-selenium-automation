Feature: Verify product added to cart

  Scenario: User can add product to cart
    Given Open Target main page
    When Search for doll
    And Click add product to cart icon
    And Confirm add to cart icon on side navigation
    And Click add to cart on nav
    And Open cart page
    Then Verify cart has 1 product