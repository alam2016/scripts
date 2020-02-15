Feature: Mercury web application login

  Background: launch mercury web app
    Given mercury web app is running


  Scenario: valid login
    When enter valid username
    And enter valid password
    And enter valid company id
    And click login
    Then login should be successful