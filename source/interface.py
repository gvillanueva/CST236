class Interface(object):
    def __init__(self):
        self.__running = True

    @property
    def running(self):
        return self.__running

    def acceptInput(self, input):
        if input == 'X':
            self.__running = False