
Feature: Text Modifiers Module

  Scenario: all_lowercased_text
    Given I have the string "all lowered"
    When I use the uppercase function
    Then I see the string "ALL LOWERED"

  Scenario: all uppercased text
    Given I have the string "ALL UPPERCASE"
    When I use the lowercase function
    Then I see the string "all uppercase"
