
Feature: Testing tasks

  @web
  Scenario: Create a new task
    Given I am in the "http://localhost:8000" page
    And I am already logged in
    When I click on the "View tasks" link
    And I click on the "Create new task" link
    And I write "TT" on the "title" field
    And I write "This is a test, please delete." on the "description" field
    And I click on the "Save" button
    Then I see a "TT" task card

  @web
  Scenario: Edit an existing task
    Given I am in the "http://localhost:8000" page
    And I am already logged in
    When I click on the "View tasks" link
    And I click on the Edit link of the "TT" task card
    And I write " 2" on the "title" field
    And I write " This has been updated." on the "description" field
    And I click on the "Save" button
    Then I see a "TT 2" task card
    And I see a "This is a test, please delete. This has been updated." task card description
