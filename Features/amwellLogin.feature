Feature: Login

  @smoke1
  Scenario: Login to amwell with valid parameters
    Given launch edge browser
    When open login page
    And enter username "vusala_yusif@yahoo.com" and password "Testing2024"
    And click login button
    Then user must successfully log in
    And close browser


  @smoke3
  Scenario Outline: Login to amwell with invalid parameters
    Given launch edge browser
    When open login page
    And enter username "<username>" and password "<password>"
    And click login button
    Then user shouldn't successfully log in
    And close browser
    Examples:
      | username               | password    |
      | vusala.yusif@yahoo.com | Testing2024 |
      | vusala_yusif@yahoo.com | Test        |
      | vusala_yosif@yahoo.com | Testing2024 |




