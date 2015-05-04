"""
:mod:`source.threat` -- Threat class
========================================

The threat class manages a threat its unique ID and priority
"""
import uuid


class Threat(object):

    """Instantiates a new Threat object, assigning initial values
    :param priority: The initial priority of the threat
    :type priority: int

    :param obj: The object tracked as a threat
    :type obj: object
    """
    def __init__(self, priority=0, obj=None):
        self.__priority = priority
        self.__obj = obj
        self.__id = uuid.uuid4()

    """Returns the threat's priority value
    :param priority: The priority of the threat
    :type priority: int
    """
    @property
    def priority(self):
        return self.__priority

    """Returns the threat's obj
    :param obj: The object monitored by the threat
    :type obj: object
    """
    @property
    def obj(self):
        return self.__obj

    """Returns the threat's id
    :param id: The globally unique identifier of the threat
    :type id: uuid
    """
    @property
    def id(self):
        return self.__id