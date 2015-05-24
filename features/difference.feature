Feature: Show speed difference
    When I enter a city, speed and hd size
    I want to see the difference in time between the network and the hard drive

Scenario: Calculation completed
  Given the city of Salem
    And a network speed of 100 MBps
    And a hard drive size of 10 MB
   When time difference is calculated
   Then return -2215.28461538461
