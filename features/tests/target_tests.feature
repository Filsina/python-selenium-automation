# Created by alex7 at 5/17/2024
Feature: Target check test

  Scenario: User can see 'Your cart is empty' message
    Given Open Target main page
    When Click on 'cart icon'
    Then Verify 'Your cart is empty' message displayed

  Scenario: User can open 'Sign In' form
    Given Open Target main page
    When Click on 'Sign In'
    When Click on 'Sign In' from right
    Then Verify Sign In form opens