Feature: Login

  Background:
    Given we have application running

  @login_as_valid
  Scenario: Login as valid user
    When login as "admin" with password "123"
    Then status must be "success"
    And token must have value

    @login_as_invalid
  Scenario: Login with invalid user credentials
    When login as "fake-user" with password "fake-password"
    Then status must be "fail"
    And token must not have value

   Scenario: Login with empty fields
    When login as " " with password " "
    Then status must be "fail"
    And token must not have value

  Scenario: Login with wrong password
    When login as "admin" with password "wrong_password"
    Then status must be "fail"
    And token must not have value

   Scenario: Login with valid username and empty password
    When login as "admin" with password " "
    Then  status must be "fail"
    And token must not have value

    Scenario: Login with empty username and valid password
    When login as " " with password "123"
    Then  status must be "fail"
    And token must not have value

  Scenario: Login with valid username and invalid password
    When login as "admin" with password "1234"
    Then  status must be "fail"
    And token must not have value

    Scenario: Login with invalid username and valid password
    When login as "Ivan" with password "123"
    Then  status must be "fail"
    And token must not have value










