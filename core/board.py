class Board:
    def __init__(self):
        self.__contenedor_fichas__ = [    #el cuadrante de arriba a la derecha es el ultimo cuandrante del jugador con fichas negras
            [0,0,0,0,0,0],[0,0,0,0,0,0],   #el cuadrante de abajo a derecha es el ultimo cuadrante para el jugador de fichas blancas
            [0,0,0,0,0,0],[0,0,0,0,0,0]]
        self.__contenedor_color__ = [
            ["","","","","",""],["","","","","",""],
            ["","","","","",""],["","","","","",""]
        ]
    
    '''Entradas: cuadrante, posición y turno actual

        Funcionalidad: Quita una ficha en una posición especifica de un cuadrante, restádole 1 a la posición y definiendo el color
    '''
    def quitar_ficha(self, cuad, pos, turno):
        self.__contenedor_fichas__[cuad][pos] = self.__contenedor_fichas__[cuad][pos] -1
        if self.__contenedor_fichas__[cuad][pos] == 0:
            self.__contenedor_color__[cuad][pos] = ""
        else:
            self.__contenedor_color__[cuad][pos] = turno
    '''Entradas: cuadrante, posición y turno actual

        Funcionalidad: Pone una ficha en una posición especifica de un cuadrante, sumándole 1 a la posición y definiendo el color
    '''
    
    def poner_ficha(self, cuad, pos, turno):
        self.__contenedor_fichas__[cuad][pos] =+ 1
        self.__contenedor_color__[cuad][pos] = turno