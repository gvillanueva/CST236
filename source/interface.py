"""
:mod:`source.interface` -- Interface class
===================================================

The interface class presents the user with options for controlling the program.
"""
import logging
import security
import threat
import random
import orc

logger = logging.getLogger(__name__)


class Interface(object):
    """Instantiates an interface class object
    """
    def __init__(self):
        self.__running = True
        self.secObj = security.Security()

    """Gets whether the interface is running or not

    :return: Flag indicating whether the interface is running
    :rtype: boolean
    """
    @property
    def running(self):
        return self.__running

    """Accepts input to the interface
    :param input: Input string to the interface
    :type input: string
    """
    def acceptInput(self, input):
        if input == 'X':
            self.__running = False
        elif input == '?':
            return '\'X\'- Quit alert system\n\'?\'- Show these instructions'
        elif input == 'demo_addorc':
            newOrc = orc.Orc(random.randint(0, 200), random.randint(0, 50))
            newThreat = threat.Threat(random.randint(1, 10), newOrc)
            self.secObj.addThreat(newThreat)
            return newThreat
        elif input == 'ENTer the Trees':
            self.secObj.resetThreats()
            return self.secObj.threatCount