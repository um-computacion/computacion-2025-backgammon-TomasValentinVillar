import random

class Dice:
    def __init__(self):
        self.__numero__ = 0
    
    def tirar_dado(self):
        self.__numero__ = random.randint(1,6)
        return self.__numero__