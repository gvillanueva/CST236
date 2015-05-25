"""
:mod:`source.speed_researcher` -- SpeedResearcher class
=======================================================

The SpeedResearcher class is the main interface into the speed researching
system.
"""
class SpeedResearcher(object):
    """Instantiates a new SpeedResearcher object.
    """
    def __init__(self):
        self._driving_speed = 0.0
        self._net_speed = 0.0
        self._hdd_size = 0.0
        self._distance = 0.0
        self._cities = {'Salem': 40}

    """Gets the value of the estimated driving speed.
    :return: The estimated driving speed.
    :rtype: float
    """
    @property
    def driving_speed(self):
        return self._driving_speed

    """Sets the value of the estimated driving speed.
    :param value: The desired value of the driving speed estimate.
    :type value: float
    """
    @driving_speed.setter
    def driving_speed(self, value):
        if isinstance(value, (float, int)) and 0 <= value <= 100000:
            self._driving_speed = float(value)
        elif value == 'Porsche':
            self._driving_speed = 200
        elif value == 'Bus':
            self._driving_speed = 65
        elif value == 'Cement Truck':
            self._driving_speed = 45
        elif value == 'Laden Swallow':
            self._driving_speed = 24

    """Gets the value of the estimated driving speed.
    :return: The estimated driving speed.
    :rtype: float
    """
    @property
    def net_speed(self):
        return self._net_speed

    """Sets the value of the estimated network speed.
    :param value: The desired value of the network speed estimate.
    :type value: float
    """
    @net_speed.setter
    def net_speed(self, value):
        if isinstance(value, (float, int)) and 0 <= value <= 100000:
            self._net_speed = float(value)

    """Gets the value of the hard drive size.
    :return: The hard drive size.
    :rtype: float
    """
    @property
    def hdd_size(self):
        return self._hdd_size

    """Sets the value of the hard drive size.
    :param value: The desired value of the hard drive size.
    :type value: float
    """
    @hdd_size.setter
    def hdd_size(self, value):
        if isinstance(value, (float, int)) and 0 <= value:
            self._hdd_size = float(value)

    """Gets the value of the distance.
    :return: The distance the data is being moved.
    :rtype: float
    """
    @property
    def distance(self):
        return self._distance

    """Set the value of the distance using the city name.
    :param value: The city name used to lookup distance.
    :type value: string
    """
    def setCity(self, name):
        if isinstance(name, str) and name in self._cities:
            self._distance = float(self._cities[name])

    """Creates a new city with the given values for name and distance
    :param name: The city name associated with distance.
    :type name: string
    :param distance: The distance to the city, in miles.
    :type distance: float
    :return: False if the city is not added
    :rtype: bool
    """
    def addCity(self, name, distance):
        if not isinstance(name, str):
            return False
        if name not in self._cities:
            self._cities[name] = distance
        else:
            return False

    """Gets the list of cities in the research system's city file
    :return: List of cities in the city file
    :rtype: list
    """
    @property
    def cities(self):
        return self._cities.keys()

    """Calculates the network speed (MBps) equivalent of driving
    :return: The MBps speed of driving
    :rtype: float
    """
    def calcDrivingMBps(self):
        return self._hdd_size / (self._distance / (self._driving_speed / 60.0 / 60.0))

    """Compares the given network speed to the calculated driving speed equivalent
    :return: -1 if network speed is faster, 1 if driving is faster, or 0, if equivalent
    """
    def compare(self):
        roundedDrivingMBps = round(self.calcDrivingMBps())
        roundedNetMBps = round(self._net_speed)
        if roundedDrivingMBps < roundedNetMBps:
            return -1
        elif roundedDrivingMBps > roundedNetMBps:
            return 1
        else:
            return 0

    """Calculates the difference in time between network and physical transfers
    :return: The time for transfer across the network subtracted from the time for transfer driving
    """
    def calcTimeDifference(self):
        drivingMBps = self.calcDrivingMBps()
        return (self._hdd_size / self._net_speed) - (self.hdd_size / drivingMBps)