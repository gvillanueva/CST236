"""
:mod:`source.interface` -- Interface class
===================================================

The interface class presents the user with options for controlling the program.
"""
import logging

logger = logging.getLogger(__name__)


class Interface(object):
    """Instantiates an interface class object
    """
    def __init__(self):
        self.__running = True

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