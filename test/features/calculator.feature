Feature: Calculator

Scenario Outline: Expression Validation
    Given I am a user of the Calculator App
    When I enter <expression>
    Then The output is <expected>


Examples: Math Expressions
    |   expression              |   expected|
    |   2 + 1 = 3               |   True    |
    |   2 + 10 = 12             |   True    |
    |   2 + 11 = 13             |   True    |
    |   2 + 101 = 3             |   False   |
    |   2 + 1093 = 12           |   False   |
    |   2 * 110 = 13            |   False   |
    |   2 - 1 = 3               |   False   |
    |   2 / 10 = 12             |   False   |
    |   2 + 11 = 13             |   True    |
    |   2 + 1 = 3               |   True    |
    |   2 + 10 = 12             |   True    |
    |   2 + 11 = 13             |   True    |