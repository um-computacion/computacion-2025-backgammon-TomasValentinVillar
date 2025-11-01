'''
Modulo encargado del valor de los dados individuales
contiene a la clase Dice
'''
import random

class Dice:
    '''
    Responsabilidad: Representa un instancia de dado
    '''
    def __init__(self):
        self.__numero__ = 0


    def tirar_dado(self):
        '''
        Funcionalidad: asignarle un valor aleatorio entre el 1 y el 6 al 
        atributo numero de Dice para simular una tirada de dados
        '''
        self.__numero__ = random.randint(1,6)

    def obtener_numero(self):
        '''
        Funcionalidad: Devolver el atributo numero de la clase Dice

        Salida: el atributo numero de Dice
        '''
        return self.__numero__
