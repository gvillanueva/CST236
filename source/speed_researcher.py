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
        self._net_speed = 0
        self._hdd_size = 0
        self._distance = 0

    """Gets the value of the estimated network speed.
    :return: The estimated network speed.
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
            self._net_speed = value

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