Feature: Preset driving speeds
    When entering the driving speed
    I would like to be able to specify some preset values (Porsche, Bus, Cement Truck, laden swallow)

Scenario: Porsche
  Given a preset driving speed of 'Porsche'
   When setting speed
   Then change the speed to 200

Scenario: Bus
  Given a preset driving speed of 'Bus'
   When setting speed
   Then change the speed to 65

Scenario: Cement Truck
  Given a preset driving speed of 'Cement Truck'
   When setting speed
   Then change the speed to 45

Scenario: Laden Swallow
  Given a preset driving speed of 'Laden Swallow'
   When setting speed
   Then change the speed to 24