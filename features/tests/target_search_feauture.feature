# Created by alex7 at 5/25/2024
Feature: Search test


  Scenario:
    Given Open Target main page
    When Search for coffee
    Then Verify search results are shown for coffee

  Scenario: Verify that user can see product names and images
    Given Open target main page
    When Search for AirPods (3rd Generation)
    Then Verify that every product has a name and an image




