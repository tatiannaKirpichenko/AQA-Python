Feature: Calculator Operations

  Background:
    Given the application is running

  Scenario: Successful login and valid addition operation
    Given valid login credentials
    When login with username "admin" and password "123"
    Then the login response status should be "success"
    And a token should be returned

    When addition with operands 5 and 3
    Then the calculation response status should be "success"
    And the result should be 8


  Scenario: Successful login and valid subtraction operation
    Given valid login credentials
    When login with username "admin" and password "123"
    Then the login response status should be "success"
    And a token should be returned

    When subtraction with operands 10 and 3
    Then the calculation response status should be "success"
    And the result should be 7


  Scenario: Successful login and valid addition of two negative numbers
    Given valid login credentials
    When login with username "admin" and password "123"
    Then the login response status should be "success"
    And a token should be returned

    When addition with operands -5 and -8
    Then the calculation response status should be "success"
    And the result should be -13


  Scenario: Successful login and valid addition of two negative numbers
    Given valid login credentials
    When login with username "admin" and password "123"
    Then the login response status should be "success"
    And a token should be returned

    When addition with operands -5 and -8
    Then the calculation response status should be "success"
    And the result should be -13


  Scenario: Successful login and valid subtraction of a negative number from a positive number
    Given valid login credentials
    When login with username "admin" and password "123"
    Then the login response status should be "success"
    And a token should be returned

    When subtraction with operands 10 and -15
    Then the calculation response status should be "success"
    And the result should be 25

  Scenario:Calculator addition operation with fractional numbers
    Given valid login credentials
    When login with username "admin" and password "123"
    Then the login response status should be "success"
    And a token should be returned

    When addition with different operands 0.5 and 0.7
    Then the response should indicate an error



  Scenario:  Calculator operation with string inputs
    Given valid login credentials
    When login with username "admin" and password "123"
    Then the login response status should be "success"
    And a token should be returned

    When addition with different operands 'string1' and 'string2'
    Then the response should indicate an error

  Scenario: Calculator division operation with two integer numbers
    Given valid login credentials
    When login with username "admin" and password "123"
    Then the login response status should be "success"
    And a token should be returned

    When division with operands 7 and 3
    Then the response should indicate a failure with a message










