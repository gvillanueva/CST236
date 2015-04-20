"""
:mod:`source.unit` -- Unit class
==============================

The Unit class is a globally available setting for specifying/unifying units of measurement
"""
import logging

logger = logging.getLogger(__name__)


class Unit(object):
    upi = 0

    """Sets the system of measurement used by Unit
    :param system: The system of measurement to be used. Unknown systems result in upi of 0.
    :type system: string
    """
    @staticmethod
    def setSystem(system):
        if system == 'imperial':
            Unit.upi = 1
        elif system == 'metric':
            Unit.upi = 25.4
        elif system == 'parsecs':
            Unit.upi = 1.21483369e18
        elif system == 'nautical':
            Unit.upi = 1.37149e-5
        else:
            Unit.upi = 0

    """Returns the units-per-inch value of the current system
    :return: Units-per-inch value of the current system
    :rtype: float
    """
    @staticmethod
    def upi():
        return Unit.upi