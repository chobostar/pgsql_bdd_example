Feature: Testing pgsql function

Scenario: Run my 1st test
    Given we have 2 integer values 3 and 5
    When call function for sum them
    Then behave will test it for us!

    Given we have 2 integer values 9 and 9
    When call function for sum them
    Then behave will test it for us!

    Given we have 2 integer values 19 and 129
    When call function for a test
    Then behave will test it for us!

    Given we have 2 integer values 1 and -1
    When call function for a test
    Then behave will test it for us!
