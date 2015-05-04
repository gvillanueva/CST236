"""
:mod:`source.security` -- Security class
========================================

The security class monitors threats and reports perimeter status.
"""
import logging
import uuid
from source.threat import Threat

logger = logging.getLogger(__name__)


class Security(object):
    """Instantiates a new Security object.
    """
    def __init__(self):
        self.__perimeter_breached = False
        self.__enemy = None
        self.__threats = { }

    """Gets whether the security perimeter has been breached.
    :return: True or false, depending on the current security status.
    :rtype: boolean
    """
    @property
    def perimeter_breached(self):
        return self.__perimeter_breached

    """Gets the enemy of the security system
    :return: The name of the enemy of the security system
    :rtype: string
    """
    @property
    def enemy(self):
        return self.__enemy

    """Sets the enemy of the security system
    :param value: The name of the enemy the system should monitor
    :type value: string
    """
    @enemy.setter
    def enemy(self, value):
        self.__enemy = value

    """Allows a subject to penetrate the security perimeter
    :param perpetrator: The perpetrator of the perimeter breach
    :type value: string

    Sets the perimeter_breached flag if the perpetrator is an enemy.
    """
    def breach_perimeter(self, perpetrator):
        if perpetrator == self.enemy:
            self.__perimeter_breached = True

    """Gets the distance of a target
    :param target: An object which must contain its distance to the security perimeter
    :type target: object

    :return: The target's distance to the perimeter.
    :rtype: int
    """
    def getDistance(self, target):
        return target.distance

    """Gets the velocity of a target
    :param target: An object which must contain its velocity
    :type target: object

    :return: The target's velocity.
    :rtype: int
    """
    def getVelocity(self, target):
        return target.velocity

    """Gets the type of a target
    :param target: An object which must contain its specialized type
    :type target: object

    :return: The target's type
    :rtype: string
    """
    def getType(self, target):
        return target.type

    """Removes a threat from the security system
    :param uuid: A unique identifier indexing a threat in the security system
    :type threatId: uuid.UUID
    """
    def removeThreat(self, threatId):
        if threatId in self.__threats:
            del self.__threats[threatId]

    """Adds a threat to the security system
    :param threat: A threat to be tracked in the security system
    :type threat: threat.Threat

    :return: A unique identifier indexing the threat in the security system, or None if threat is not a Threat.threat.
    :rtype: uuid.UUID
    """
    def addThreat(self, threat):
        if not isinstance(threat, Threat):
            return None

        threatId = uuid.uuid4()
        self.__threats[threatId] = threat
        return threatId

    """Determines whether a given threatId is being tracked
    :param threatId: A unique id indexing a threat
    :type threatId: uuid.UUID

    :return: True if threatId is contained, otherwise false
    :rtype: boolean
    """
    def containsThreat(self, threatId):
        return threatId in self.__threats

    """Gets the number of threats being tracked.
    :param threatCount: The number of threats being tracked.
    :type threatCount: int
    """
    @property
    def threatCount(self):
        return len(self.__threats)

    """Resets the threat dictionary
    """
    def resetThreats(self):
        self.__threats = {}

    """Finds a threat's priority using its UUID
    :param threatId: A unique id indexing a threat
    :type threatId: uuid.UUID

    :return: Returns the priority of the threat, if it exists in the threats dictionary. Otherwise, returns 0.
    :rtype: int
    """
    def getPriority(self, threatId):
        if threatId not in self.__threats:
            return 0

        return self.__threats[threatId].priority