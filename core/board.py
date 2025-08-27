from core.checker import Checker

class Board:
    def __init__(self):
        self.__contenedor_fichas__ = [
            [],[],[],[],[],[], [],[],[],[],[],[],
            [],[],[],[],[],[], [],[],[],[],[],[]
        ]
        
    
    '''Entradas: cuadrante, posición y turno actual

        Funcionalidad: Quita una ficha en una posición especifica de un cuadrante, restádole 1 a la posición y definiendo el color
    '''
    def quitar_ficha(self,pos):
        self.__contenedor_fichas__[pos].pop()  
    
    def poner_ficha(self, pos, turno):

        self.__contenedor_fichas__[pos].append(Checker(turno))