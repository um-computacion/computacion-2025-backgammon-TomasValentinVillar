from core.board import Board
from core.dice import Dice
class PosNoDisponible(Exception):
    pass
class NoHayMovimientosPosibles(Exception):
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
    

    def verificar_posicion_disponible(self,posicion):

        board = self.__board__.__contenedor_fichas__
        if (len(board[posicion]) >= 1 and board[posicion][0].obtener_color()== self.__turno__) or len(board[posicion]) == 0:
                    return True
        raise PosNoDisponible('Posicion no disponible')
    
    def verifificar_movimientos_posibles(self):
         '''

         Funcionalidad: verifica hay al menos un movimiento posible segun las posiciones del tablero y los numeros de los dados

         Salida: True si hay al menos un movimeto posible o Exepcion NoHayMovimientosPosibles si no hay movimientos posibles
         '''
         board = self.__board__.__contenedor_fichas__
         d1 = self.__dice_1__
         d2 = self.__dice_2__
         
         bandera = False
         for i in range(0,24):
            if board[i] != []:
                if (len(board[i+d1]) >= 1 and board[i+d1][0].obtener_color()== self.__turno__) or len(board[i+d1]) == 0:
                        bandera = True
         for i in range(0,24):
            if board[i] != []:
                if (len(board[i+d2]) >= 1 and board[i+d2][0].obtener_color()== self.__turno__) or len(board[i+d2]) == 0:
                        bandera = True
         for i in range(0,24):
            if board[i] != []:
                if (len(board[i+d2+d1]) >= 1 and board[i+d2+d1][0].obtener_color()== self.__turno__) or len(board[i+d2+d1]) == 0:
                    bandera = True
         if bandera == True:
              return True
         else:
              raise NoHayMovimientosPosibles("No hay movimientos posibles")


              '''if board[i] != []:
                    self.verificar_posicion_disponible(i+d1)
                    self.verificar_posicion_disponible(i+d2)
                    self.verificar_posicion_disponible(i+d1+d2)'''