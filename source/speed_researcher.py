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
        self._driving_speed= 0
        self._hdd_size = 0
        self._distance = 0

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
            self._driving_speed = value

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
            self._hdd_size = value

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
    @distance.setter
    def distance(self, value):
        if isinstance(value, str) and value == 'Salem':
            self._distance = 40

    def compare(self):
        physTransferSpeed = self.hdd_size * (self._distance / 216000)
        return