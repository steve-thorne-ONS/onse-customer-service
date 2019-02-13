Feature: Create customer

  Scenario: A recently married customer wants to change surname
    Given customer "Gene Kim" with ID "12345" exists
    When customer with ID "12345" changes their surname to "Smith"
    Then Account "12345" now has name "Gene Smith"
