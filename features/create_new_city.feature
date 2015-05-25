Feature: Create new cities
    When selecting a city
    I want to be able to create a new city
    so I have more options

    When I enter a new city,
    I want the results to be written to the city file

  Scenario: New city
    Given the city of 'Eugene'
      And a distance of 111 mi
     When 'Eugene' does not already exist
      And a new city is created for 'Eugene'
     Then a city is added for 'Eugene'
      And the new city is added to the city file

  Scenario: City already exists
    Given the city of 'Salem'
      And a distance of 111 mi
     When 'Salem' already exists
      And a new city is created for 'Salem'
     Then False is returned

  Scenario: City name is not a string
    Given the city of 1.948
      And a distance of 111 mi
     When adding a city for 1.948
     Then False is returned
      And no city is added
