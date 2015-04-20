class Orc(object):
    def __init__(self, distance=0, velocity=0):
        self.__distance = distance
        self.__velocity = velocity

    @property
    def distance(self):
        return self.__distance

    @property
    def velocity(self):
        return self.__velocity