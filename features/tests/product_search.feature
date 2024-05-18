Feature: Cart check test

  Scenario: User can see 'Your cart is empty' message
    Given Open Target main page
    When Click on 'cart icon'
    Then Verify 'Your cart is empty' message displayed
