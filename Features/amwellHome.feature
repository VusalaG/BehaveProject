Feature: Amwell

  @smoke1
  Scenario: Logo presence on amwell home page
    Given launch edge browser
    When open amwell home page
    Then verify the logo of the home page
    And close browser

  @smoke2
  Scenario: Verify the login url
    Given launch edge browser
    When open amwell home page
    And click on sign in button
    Then verify url of the login page
    And close browser
