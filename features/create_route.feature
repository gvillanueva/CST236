Feature: Specify path route
    When researching speed
    I want to be able to create a route of 1 - 10 cities
    so I can get a more accurate picture

  Scenario: Route valid
    Given an instantiated research system
      And a route of 4 cities
      And all cities in the route exist
      And no adjacent elements are the same city
     When requesting the system to use our route
     Then True is returned

  Scenario: More than 10 cities
    Given an instantiated research system
      And a route of 11 cities
      And all cities in the route exist
      And no adjacent elements are the same city
     When requesting the system to use our route
     Then False is returned

  Scenario: No cities
    Given an instantiated research system
      And a route of no cities
     When requesting the system to use our route
     Then False is returned

  Scenario: Route contains unknown city
    Given an instantiated research system
      And a route of 3 cities, containing an unknown city
      And no adjacent elements are the same city
     When requesting the system to use our route
     Then False is returned

  Scenario: City-to and City-from are the same city
    Given an instantiated research system
      And a route of 2 of the same cities
      And all cities in the route exist
     When requesting the system to use our route
     Then False is returned
