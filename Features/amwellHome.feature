Feature: Amwell Logo

  Scenario: Logo presence on amwell home page
    Given launch edge browser
    When open amwell home page
    Then verify that logo presence on the page
    And close browser

