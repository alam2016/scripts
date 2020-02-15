Feature: Calculate operations

    Scenario: addition
      Given calculate app is running
      When calling add function to add 5 and 2
      Then calculate app should return 7

    Scenario: subtraction
      Given calculate app is running
      When calling subtraction function to subtract 5 and 2
      Then calculate app should return 3

    Scenario Outline: subtraction positive and negative data
      Given calculate app is running
      When calling subtraction function to subtract <x> and <y>
      Then calculate app should return <r>

      Examples: Data
      |x|y|r|
      |5|2|3|
      |2|5|-3|
      |5|5|0|

    Scenario: multiplication
      Given calculate app is running
      When calling multiplication function to multiply 5 and 2
      Then calculate app should return 10

    Scenario Outline: division
      Given calculate app is running
      When calling division function to divide <x> and <y>
      Then calculate app should return <r>

      Examples: Data
      |x|y|r|
      |10|2|5|
      |2|10|0|
      |4|4|1|
