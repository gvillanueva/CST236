Feature: Create new cities
    When I start the application
    I want to enter my starting city
    so I know where I am

  Scenario: City exists
    Given the starting city of 'Portland'
     When the system is created
     Then SpeedResearcher constructor returns SpeedResearcher instance

  Scenario: City does not exist
    Given the starting city of 'Tacna'
     When the system is created
     Then SpeedResearcher constructor raises ValueError

  Scenario: City name is not a string
    Given the starting city of 1.948
     When the system is created
     Then SpeedResearcher constructor raises ValueError
