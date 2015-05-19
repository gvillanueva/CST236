Feature: Show best option
    When I enter a city, a speed and hard drive size
    I want to see whether the network or the hard drive would be faster

Scenario: Valid triplet, network is faster
  Given the city of Salem
    And a speed of 100 MBps
    And a hard drive size of 10 MB
   When compare is requested
   Then return -1

Scenario: Valid triplet, driving is faster
  Given the city of Salem
    And a speed of 1 MBps
    And a hard drive size 10000 MB
   When compare is requested
   Then return 1

Scenario: Valid triplet, methods are equal
  Given the city of Salem
    And a speed of 1 MBps
    And a hard drive size of 2400 MB
   When compare is requested
   Then return 0
