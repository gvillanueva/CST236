Feature: Show best option
    When I enter a city, a speed and hard drive size
    I want to see whether the network or the hard drive would be faster

Scenario: Valid params, network is faster
  Given the city of Salem
    And a network speed of 100 MBps
    And a hard drive size of 10 MB
   When compare is requested
   Then return -1

Scenario: Valid params, driving is faster
  Given the city of Salem
    And a network speed of 1 MBps
    And a hard drive size of 1000000 MB
   When compare is requested
   Then return 1

Scenario: Valid params, methods are equal
  Given the city of Salem
    And a network speed of 1 MBps
    And a hard drive size of 2215.38461538461 MB
   When compare is requested
   Then return 0
