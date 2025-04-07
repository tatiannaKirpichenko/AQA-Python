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

    When I perform addition with operands " " and " "
    Then I should receive an error response

  Scenario: Successful login and handling of addition of two fractional numbers
    Given I have valid login credentials
    When I login with username "admin" and password "123"
    Then the login response status should be "success"
    And a token should be returned

    When I perform addition with operands "0.5" and "0.7"
    Then I should receive an error response

  Scenario: Successful login and handling of division of two integer numbers
    Given I have valid login credentials
    When I login with username "admin" and password "123"
    Then the login response status should be "success"
    And a token should be returned

    When I perform division with operands "7" and "5"
    Then I should receive an error response











