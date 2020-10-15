
Feature: Using the searchbar and donation button
  Scenario: Do a search query using a text
    Given I am in the "https://python.org" page
    When I write "Python 3" on the searchbar
    And I click on the GO button
    Then I see a "Search Python.org" message

  Scenario: Do a search query without any text
    Given I am in the "https://python.org" page
    When I click on the GO button
    Then I see a "Search Python.org" message

  Scenario: Go to the donation page
    Given I am in the "https://python.org" page
    When I click on the donation link
    Then I am in the "https://psfmember.org/" page
