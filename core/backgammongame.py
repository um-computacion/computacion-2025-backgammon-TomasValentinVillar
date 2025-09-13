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
        self.__dados_disponibles__ = []

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
        if self.__turno__ == 'Blanco': #corregir, debe cambiar de turno despues d que no queden movimientos
            self.__turno__ = 'Negro'
        else:
            self.__turno__ = 'Negro'
    '''

        Funcionalidad: Llama a la función tirar dado para asignarle un numero a los atributos de __dice_1__ y __dice_2__
        '''
    def tirar_dados(self):
        self.__dice_1__.tirar_dado()
        self.__dice_2__.tirar_dado()

        if self.__dice_1__.obtener_numero() == self.__dice_2__.obtener_numero():
            self.__dados_disponibles__ = [self.__dice_1__,self.__dice_2__,self.__dice_1__,self.__dice_2__]
        else:
            self.__dados_disponibles__ = [self.__dice_1__,self.__dice_2__]
        

    def verificar_posicion_disponible(self,posicion):

        board = self.__board__.__contenedor_fichas__
        if len(board[posicion]) == 0:
             return True
        elif board[posicion][0].obtener_color()== self.__turno__:
             return True
        elif len(board[posicion]) == 1: #comer ficha
             return True 
        else:
            return False

    def verificar_sacar_ficha(self, posicion, board):
        if self.__turno__ == "Blanco":
            # Blancas: verificar si está en home board (18-23)
            if posicion < 18:
                return True
            # Verificar que no hay fichas blancas fuera del home board (0-17)
            for pos in range(18):
                if len(board[pos]) > 0:
                    if board[pos][0].obtener_color() == self.__turno__:
                        raise MovimientoInvalido("No se puede realizar ese movimiento")
        else:  # Turno negro
            # Negras: verificar si está en home board (0-5)  
            if posicion > 5:
                return True
            # Verificar que no hay fichas negras fuera del home board (6-23)
            for pos in range(6, 24):
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
            
                # Calcular destino según el color
            if self.__turno__ == "Blanco":
                pos_destino = pos_origen + pasos  # Blancas van hacia arriba (0->23)
            else:  # Negro
                pos_destino = pos_origen - pasos  # Negras van hacia abajo (23->0)
    
            # Verificar límites
            if pos_destino < 0 or pos_destino >= 24:
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
                if es_movimiento_valido(i, d1.obtener_numero()) or es_movimiento_valido(i, d2.obtener_numero()):
                    return True
    
        # Verificar movimiento combinado (solo si no son dobles)
        if d1.obtener_numero() != d2.obtener_numero():
            for i in range(24):
                if es_movimiento_valido(i, d1.obtener_numero() + d2.obtener_numero()):
                    return True
    
        # Si no hay movimientos posibles, lanzar excepción
        raise NoHayMovimientosPosibles("No hay movimientos posibles")
    
    def verificar_movimientos_y_dados(self, pos_inic,pos_fin):
        d1 = self.__dice_1__
        d2 = self.__dice_2__
        

        if self.__turno__ == "Blanco":
            if (pos_fin - pos_inic) == d1.obtener_numero():
                self.__dados_disponibles__.remove(d1)
                return True
            if (pos_fin - pos_inic) == d2.obtener_numero():
                self.__dados_disponibles__.remove(d2)
                return True
            if (pos_fin - pos_inic) == d1.obtener_numero() + d2.obtener_numero():
                self.__dados_disponibles__.remove(d1)
                self.__dados_disponibles__.remove(d2)
                return True
            else:
                raise MovimientoInvalido("El moviemiento no coincide con el dado")
            
        elif self.__turno__ == "Negro":
            if (pos_inic - pos_fin) == d1.obtener_numero():
                self.__dados_disponibles__.remove(d1)
                return True
            if (pos_inic - pos_fin) == d2.obtener_numero():
                self.__dados_disponibles__.remove(d2)
                return True
            if (pos_inic - pos_fin) == d1.obtener_numero() + d2.obtener_numero():
                self.__dados_disponibles__.remove(d1)
                self.__dados_disponibles__.remove(d2)
                return True
            else:
                raise MovimientoInvalido("El moviemiento no coincide con el dado")
    

    

    #funcion realizar moviemto, se puede hacer una funcion aparte o agregar funcionalidad a funcion, acá cuando se haga un moviemmiton 
    # se fijará si se puede hacer el movimiento segun el dado y sabrá sobre la cantidad de movimientos posibles
         
    #función que verifica ganador    

    