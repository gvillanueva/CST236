"""
:mod:`source.orc` -- Orc class
==============================

The Orc class identifies an orc creature, including its distance, velocity and type.
"""
import logging

logger = logging.getLogger(__name__)


class Orc(object):
    """Instantiate a new Orc object.

    :param distance: Distance from orc to perimeter
    :type distance: int

    :param velocity: Velocity of the orc creature
    :type velocity: int

    :param type: The type of the orc creature
    :type type: string
    """
    def __init__(self, distance=0, velocity=0, type='builder'):
        self.__distance = distance
        self.__velocity = velocity
        self.__type = type
        self.__isAlive = True       # Orc is always alive when created

    """Gets the value of the orc's distance
    :return: A value indicating the distance of the creature from the perimeter
    :rtype: int
    """
    @property
    def distance(self):
        return self.__distance

    """Gets the value of the orc's velocity
    :return: A value indicating the orc's velocity
    :rtype: int
    """
    @property
    def velocity(self):
        return self.__velocity

    """Gets the type of the orc
    :return: A string identifying the orc's type
    :rtype: string
    """
    @property
    def type(self):
        return self.__type

    """Gets whether the orc is alive or not
    :return: A flag indicating alive or not
    :rtype: boolean
    """
    @property
    def isAlive(self):
        return self.__isAlive

    """Kills the orc, setting isAlive to False.
    """
    def kill(self):
        self.__isAlive = False