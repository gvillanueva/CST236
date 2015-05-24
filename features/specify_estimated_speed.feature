Feature: Specify Estimated Driving Speed
    When researching speeds
    I want to be able to select an estimated speed
    so I can see whether the network or driving would be faster

Scenario: Valid estimated driving speed
    Given a speed between 0 and 200 MPH
     When setting speed
     Then change the speed setting

Scenario: Estimated driving speed too high
    Given a speed greater than 200 MPH
     When setting speed
     Then do not change the speed setting

Scenario: Estimated driving speed too low
    Given a speed less than 0 MPH
     When setting speed
     Then do not change the speed setting

Scenario: Estimated driving speed not a float
  Given a speed of 'One hundred MPH'
   When setting speed
   Then do not change the speed setting
