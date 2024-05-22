Feature: Target circle page test

  Scenario: User can see 10 benefit cells
    Given Open Target main page
    When Search for Target circle icon
    Then Verify header in shown

  Scenario: Verify header has correct amount links
    Given Open Target main page
    Then Verify header has 10 links