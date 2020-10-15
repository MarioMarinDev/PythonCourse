
  Feature: Text Modifiers Module

    Scenario: all lowercased text to uppercase
      Given I have the string "my text"
      When I use the uppercase function
      Then I see the string "MY TEXT"

    Scenario: mixed cased text to uppercase
      Given I have the string "My TexT"
      When I use the uppercase function
      Then I see the string "MY TEXT"

    Scenario: all uppercased text to uppercase
      Given I have the string "HELLO"
      When I use the uppercase function
      Then I see the string "HELLO"

    Scenario: all uppercased text to lowercase
      Given I have the string "MY TEXT"
      When I use the lowercase function
      Then I see the string "my text"

    Scenario: mixed cased text to lowercase
      Given I have the string "My TexT"
      When I use the lowercase function
      Then I see the string "my text"

    Scenario: all loweredcased text to lo lowercase
      Given I have the string "hello"
      When I use the lowercase function
      Then I see the string "hello"

    Scenario: some text with numbers and letters and get just the numbers
      Given I have the string "H1E2L3L4O5"
      When I use the only numbers function
      Then I see the string "12345"

    Scenario: Some text without numbers and get just the numbers
      Given I have the string "123456789"
      When I use the only numbers function
      Then I see the string "123456789"

    Scenario: Only letters text and get just the numbers
      Given I have the string "Hello"
      When I use the only numbers function
      Then I see the string ""
