
Feature: Using the searchbar and donation button

  @web
  Scenario: Do a search query without text
    Given I am in the "https://python.org" page
    When I click on the GO button
    Then I see a "Search Python.org" message

  @web
  Scenario: Go to the donation page
    Given I am in the "https://python.org" page
    When I click on the donation button
    Then I am in the "https://psfmember.org" page

  @web
  Scenario: Do a search query with text
    Given I am in the "https://python.org" page
    When I write "Python 3" on the searchbar
    And I click on the GO button
    Then I see a "Search Python.org" message
