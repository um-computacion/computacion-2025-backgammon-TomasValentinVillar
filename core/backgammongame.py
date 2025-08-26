from core.board import Board
from core.dice import Dice
class PosNoDisponible(Exception):
    pass
class BackgammonGame:
    def __init__(self):
        self.__turno__ = "B"
        self.__board__ = Board()
        self.__dice_1__ = Dice()
        self.__dice_2__ = Dice()
    '''Entradas: cuadrante inicial, posición inicial,cuadrante final, posición final y turno actual

        Funcionalidad: Utiliza las funciones quitar_ficha y poner_ficha para hacer el movimiento de la ficha de una casilla a otra
    '''
    def ocupar_casilla(self,cuand_inic, pos_inic,cuad_fin,pos_fin):
        self.__board__.quitar_ficha(cuand_inic,pos_inic,self.__turno__)
        self.__board__.poner_ficha(cuad_fin,pos_fin,self.__turno__)
        if self.__turno__ == 'B':
            self.__turno__ = 'N'
        else:
            self.__turno__ = 'N'
    '''

        Funcionalidad: Llama a la función tirar dado para asignarle un numero a los atributos de __dice_1__ y __dice_2__
        '''
    def tirar_dados(self):
        self.__dice_1__.tirar_dado()
        self.__dice_2__.tirar_dado()
    '''
    def calcular_posiciones_de_dados(self):
        if self.__turno__ == "B":
            d1 = self.__dice_1__ - 1
            d2 = self.__dice_1__ -1
    '''    
    
    def verificar_posicion_disponible(self,cuadrante,posicion):

        board = self.__board__.__contenedor_fichas__
        if (posicion >= 1 and self.__board__.__contenedor_color__[cuadrante][posicion]== self.__turno__) or board[cuadrante][posicion] == 0:
                    return True
        raise PosNoDisponible('Posicion no disponible')
            
        
    

        