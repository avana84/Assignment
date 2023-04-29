Feature: Sign in and sign up flow

  Scenario: User signs in with valid credentials and tries to register on Booking homepage
    Given Open Booking page
    When the user clicks on Sign in button
    And enters their email address "avisekruna@yahoo.com" in the email address field
    And clicks on the Continue with email button
    And enters their password "Password12k" in the login password field
    Then clicks on the Sign in button
    # Then the user should be redirected to the user account page


  Scenario: User can Register
    Given Open Booking page
    When the user clicks on Register button
    And the user enters their email address "avisekruna@yahoo.com" in the email address field
    And clicks on the Continue with email button to register
    And enters their password "Password12k" in the registration password field
    And clicks on the Sign up button
    # Then the user should be redirected to their account page