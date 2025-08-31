from core.board import Board
from core.dice import Dice
class PosNoDisponible(Exception): #esta exepción se va a usar cuando verificar_posicion_disponible sea Falsa
    pass
class NoHayMovimientosPosibles(Exception):
    pass
class MovimientoInvalido(Exception):
    pass
class BackgammonGame:
    def __init__(self):
        self.__turno__ = "Blanco"
        self.__board__ = Board()
        self.__dice_1__ = Dice()
        self.__dice_2__ = Dice()

    def ocupar_casilla(self,pos_inic,pos_fin):
        '''Entradas: cuadrante inicial, posición inicial,cuadrante final, posición final y turno actual

        Funcionalidad: Utiliza las funciones quitar_ficha y poner_ficha para hacer el movimiento de la ficha de una casilla a otra
        '''

        board = self.__board__.__contenedor_fichas__

        self.__board__.quitar_ficha(pos_inic)
        if len(board[pos_fin]) == 1: #Ahora tambien se puede comer ficha
            if board[pos_fin][0].obtener_color() != self.__turno__:
                board[pos_fin].pop()

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
        if len(board[posicion]) == 0:
             return True
        elif board[posicion][0].obtener_color()== self.__turno__:
             return True
        elif len(board[posicion]) == 1:
             return True 
        else:
            return False

    def verificar_sacar_ficha(self,posicion,board):

        if posicion < 23:
            return True

        for pos in range(18):
            if len(board[pos]) > 0:
                if board[pos][0].obtener_color() == self.__turno__:
                    raise MovimientoInvalido("No se puede realizar ese movimiento")
        
        return True
    
    def verifificar_movimientos_posibles(self):
        '''

        Funcionalidad: verifica hay al menos un movimiento posible segun las posiciones del tablero y los numeros de los dados

        Salida: True si hay al menos un movimeto posible o Exepcion NoHayMovimientosPosibles si no hay movimientos posibles
        '''
        board = self.__board__.__contenedor_fichas__
        d1 = self.__dice_1__
        d2 = self.__dice_2__

        # Función auxiliar para verificar si un movimiento es válido
        def es_movimiento_valido(pos_origen, pasos):
            # Verificar límites del tablero
            pos_destino = pos_origen + pasos
            if pos_destino >= 24:
                return False
        
            # Verificar que hay fichas del jugador actual en la posición origen
            if len(board[pos_origen]) == 0:
                return False
        
            if board[pos_origen][0].obtener_color() != self.__turno__:
                return False
        
            # Usar la función existente para verificar posición destino
            return self.verificar_posicion_disponible(pos_destino)
    
            # Verificar movimientos posibles con cada dado individualmente
        for i in range(24):
                if es_movimiento_valido(i, d1) or es_movimiento_valido(i, d2):
                    return True
    
        # Verificar movimiento combinado (solo si no son dobles)
        if d1 != d2:
            for i in range(24):
                if es_movimiento_valido(i, d1 + d2):
                    return True
    
        # Si no hay movimientos posibles, lanzar excepción
        raise NoHayMovimientosPosibles("No hay movimientos posibles")
         
        

        