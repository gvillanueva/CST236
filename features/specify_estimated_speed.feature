Feature: Specify Estimated Network Speed
    When researching speeds
    I want to be able to select an estimated speed
    so I can see whether the network or driving would be faster

Scenario: Valid estimated speed
    Given a speed between 0 and 100,000 MBps
     When setting speed
     Then change the speed setting

Scenario: Estimated speed too high
    Given a speed greater than 100,000 MBps
     When setting speed
     Then do not change the speed setting

Scenario: Estimated speed too low
    Given a speed less than 0 MBps
     When setting speed
     Then do not change the speed setting

Scenario: Estimated speed not a float
  Given a speed of 'One hundred MBps'
   When setting speed
   Then do not change the speed setting
