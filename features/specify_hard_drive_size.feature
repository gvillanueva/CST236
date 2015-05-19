Feature: Specify Hard Drive Size
    When researching speeds
    I want to be able to select a hard drive size (in GB)
    so I can have more data

Scenario: Valid hard drive size
  Given a hard drive size greater than 0 MB
   When setting hard drive size
   Then change the hard drive size

Scenario: Hard drive size less than 0
  Given a hard drive size less than 0 MB
   When setting hard drive size
   Then do not change the hard drive size

Scenario: Hard drive size is not float
  Given a hard drive size of '100 megabytes'
   When setting hard drive size
   Then do not change the hard drive size

