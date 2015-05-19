Feature: File Input
    When researching speeds,
    I want the cities, distances and connections speeds to be read from a file

Scenario: File found and valid
    Given a path to valid file
     When reading the file
     Then return the parsed data

Scenario: File found, but invalid format
    Given a path to invalid file
     When reading the file
     Then return None

Scenario: File not found
    Given a path to missing file
     When reading the file
     Then return None