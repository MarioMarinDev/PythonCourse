
Feature: Testing loging

  @web
  Scenario: Invalid credentials
    Given I am in the "http://localhost:8000" page
    And I click on the login button
    When I write "hola@hola.adios" on the email field
    And I write "asdf" on the password field
    And I click on the login button
    Then I see a "These credentials do not match our records." message

  @web
  Scenario: Valid credentials
    Given I am in the "http://localhost:8000" page
    And I click on the login button
    When I write "MarioMarin_25@outlook.com" on the email field
    And I write "123456789" on the password field
    And I click on the login button
    Then I see a "HOME" message