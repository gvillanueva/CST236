Feature: Network Latency Compensation
    When researching speeds
    I want to be able to account for network latency
    so that my numbers are more accurate.

  Scenario: Network latency greater than 0ms
    Given network latency of 90ms
     When network latency is specified as given value
     Then change network latency to given value

  Scenario: Network latency equal to 0ms
    Given network latency of 0ms
     When network latency is specified as given value
      And old network latency is 10ms
     Then change network latency to given value

  Scenario: Network latency less than 0ms
    Given network latency of -10ms
     When network latency is specified as given value
     Then do not change network latency

  Scenario: Network latency less than 100,000ms
    Given network latency of 100,000ms
     When network latency is specified as given value
     Then change network latency to given value

  Scenario: Network latency less than 100,001ms
    Given network latency of 100,001ms
     When network latency is specified as given value
     Then do not change network latency

  Scenario: Network latency not an integer
    Given network latency of 1.948ms
     When network latency is specified as given value
     Then raise a ValueError
