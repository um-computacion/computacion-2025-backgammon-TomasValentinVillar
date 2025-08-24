import random

class Dice:
    def __init__(self):
        self.__numero__ = 0
    
    '''
        Funcionalidad: asignarle un valor aleatorio entre el 1 y el 6 al atributo numero de Dice para simular una tirada de dados
    '''
    def tirar_dado(self):
        self.__numero__ = random.randint(1,6)
        
    '''
        Funcionalidad: Devolver el atributo numero de la clase Dice

        Salida: el atributo numero de Dice
    '''
    def obtener_numero(self):
        return self.__numero__