Feature: HDD Speed Selection
    When When selecting a hard drive
    I want to enter the hard drive speed (gb/s) to account for the time to copy.

  Scenario: HDD speed of 1gb/s
    Given HDD speed of 1gb/s
     When selecting a hard drive with given speed
     Then set hard drive speed

  Scenario: HDD speed less than 1000gb/s
    Given HDD speed of 1000gb/s
     When selecting a hard drive with given speed
     Then set hard drive speed

  Scenario: HDD speed equal to 0gb/s
    Given HDD speed of 0gb/s
     When selecting a hard drive with given speed
     Then raise ValueError

  Scenario: HDD speed greater than 1000gb/s
    Given HDD speed of 1001gb/s
     When selecting a hard drive with given speed
     Then raise ValueError

  Scenario: HDD speed not an integer
    Given HDD speed of 1.948
     When selecting a hard drive with given speed
     Then raise a ValueError
