Feature: Calculator Operations

  Background:
    Given the application is running

  Scenario: Successful login and valid addition operation
    Given I have valid login credentials
    When I login with username "admin" and password "123"
    Then the login response status should be "success"
    And a token should be returned

    When I perform addition with operands 5 and 3
    Then the calculation response status should be "success"
    And the result should be 8


  Scenario: Successful login and valid subtraction operation
    Given I have valid login credentials
    When I login with username "admin" and password "123"
    Then the login response status should be "success"
    And a token should be returned
    When I perform subtraction with operands 10 and 3
    Then the calculation response status should be "success"
    And the result should be 7


  Scenario: Successful login and valid addition of two negative numbers
    Given I have valid login credentials
    When I login with username "admin" and password "123"
    Then the login response status should be "success"
    And a token should be returned

    When I perform addition with operands -5 and -8
    Then the calculation response status should be "success"
    And the result should be -13


  Scenario: Successful login and valid addition of two negative numbers
    Given I have valid login credentials
    When I login with username "admin" and password "123"
    Then the login response status should be "success"
    And a token should be returned

    When I perform addition with operands -5 and -8
    Then the calculation response status should be "success"
    And the result should be -13


  Scenario: Successful login and valid subtraction of a negative number from a positive number
    Given I have valid login credentials
    When I login with username "admin" and password "123"
    Then the login response status should be "success"
    And a token should be returned

    When I perform subtraction with operands 10 and -15
    Then the calculation response status should be "success"
    And the result should be 25


  Scenario: Successful login and handling of empty inputs
    Given I have valid login credentials
    When I login with username "admin" and password "123"
    Then the login response status should be "success"
    And a token should be returned

    When the user attempts to perform a calculation with empty values
    Then the response should indicate an error

  Scenario: User attempts to add two fractional numbers after logging in
    Given I have valid login credentials
    When I login with username "admin" and password "123"
    Then the login response status should be "success"
    And a token should be returned

    When the user attempts to calculate the sum of two fractional numbers
    Then the response should indicate an error

  Scenario: User attempts to divide two integers and receives a failure response
    Given I have valid login credentials
    When I login with username "admin" and password "123"
    Then the login response status should be "success"
    And a token should be returned

    When I perform division with operands 7 and 5
    Then the response should indicate a failure with a message








