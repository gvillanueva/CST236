import logging

logger = logging.getLogger(__name__)

class Security(object):
    def __init__(self):
        self.__perimeter_breached = False
        self.__enemy = None

    @property
    def perimeter_breached(self):
        return self.__perimeter_breached

    @property
    def enemy(self):
        return self.__enemy

    @enemy.setter
    def enemy(self, value):
        self.__enemy = value

    def breach_perimeter(self, perpetrator):
        if perpetrator == self.enemy:
            self.__perimeter_breached = True

    def getDistance(self, target):
        return target.distance

    def getVelocity(self, target):
        return target.velocity