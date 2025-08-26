from core.board import Board
from core.dice import Dice
class PosNoDisponible(Exception):
    pass
class BackgammonGame:
    def __init__(self):
        self.__turno__ = "Blanco"
        self.__board__ = Board()
        self.__dice_1__ = Dice()
        self.__dice_2__ = Dice()
    '''Entradas: cuadrante inicial, posición inicial,cuadrante final, posición final y turno actual

        Funcionalidad: Utiliza las funciones quitar_ficha y poner_ficha para hacer el movimiento de la ficha de una casilla a otra
    '''
    def ocupar_casilla(self,pos_inic,pos_fin):
        self.__board__.quitar_ficha(pos_inic)
        self.__board__.poner_ficha(pos_fin,self.__turno__)
        if self.__turno__ == 'Blanco':
            self.__turno__ = 'Negro'
        else:
            self.__turno__ = 'Negro'
    '''

        Funcionalidad: Llama a la función tirar dado para asignarle un numero a los atributos de __dice_1__ y __dice_2__
        '''
    def tirar_dados(self):
        self.__dice_1__.tirar_dado()
        self.__dice_2__.tirar_dado()
    '''
    def verificar_posicion_disponible(self,cuadrante,posicion):

        board = self.__board__.__contenedor_fichas__
        if (posicion >= 1 and self.__board__.__contenedor_color__[cuadrante][posicion]== self.__turno__) or board[cuadrante][posicion] == 0:
                    return True
        raise PosNoDisponible('Posicion no disponible')
    
    def verifificar_movimiento_posible_blanco(self):
        
         board = self.__board__.__contenedor_fichas__
         for i in range(0,4):      #esta funcion hará que se recorra la tabla segun el orden del juego
                                    # en lugar de recorrerla en el orden lietaral de la lista
            if i == 0:
                cuad = board[1]
            elif i== 1:
                 cuad = board[0]
            for pos in reversed(cuad):
                j = 5
                if pos != 0 and self.__board__.__contenedor_color__ == "B":
                    
                     pass
                j -= 1
            else:
                cuad = board[i]
    '''