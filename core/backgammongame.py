from core.board import Board
from core.models.dice import Dice
from core.models.player import Player
from core.services.dice_manager import DiceManager
from core.validators.move_validator import MoveValidator
from core.validators.rule_validator import RuleValidator
class PosNoDisponible(Exception): #esta exepción se va a usar cuando verificar_posicion_disponible sea Falsa
    pass
class NoHayMovimientosPosibles(Exception):
    pass
class MovimientoInvalido(Exception):
    pass
class Ganador(Exception):
    pass

class BackgammonGame:
    def __init__(self):
        self.__turno__ = "Blanco"
        self.__board__ = Board()
        self.__dice_1__ = Dice()
        self.__dice_2__ = Dice()
        self.__dice_manager__ = DiceManager(self.__dice_1__, self.__dice_2__)
        self.__dados_disponibles__ = []
        self.__players__ = {}
        self.__move_validator__ = MoveValidator()
        self.__rule_validator__ = RuleValidator()
    
    
    def crear_jugador(self,nom,ficha,estado):
        '''Entradas: nombre de jugador, ficha correspondiente, estado inicial

        Funcionalidad: Crear una instacia de la clase jugador y agregarla en el diccionario jugadores
        '''

        jugador = Player(nom,ficha,estado)
        self.__players__[ficha] = jugador

    def obtener_players(self):
        return self.__players__

    
        
    def obtener_turno(self):
        return self.__turno__

    def obtener_board(self):
        return self.__board__
    
    def realizar_movimiento(self,pos_inic,pos_fin):
        if (len(self.__board__.obtener_contenedor_fichas()[pos_inic]) == 0) or (self.__board__.obtener_contenedor_fichas()[pos_inic][0].obtener_color() != self.__turno__):
            raise MovimientoInvalido("No se puede realizar ese moviemto")
        if (pos_fin == -1) or (pos_fin == 24):
            self.verificar_sacar_ficha(pos_inic,self.__board__.obtener_contenedor_fichas())
            self.__board__.sacar_ficha(pos_inic,self.__turno__)
        else:
            if self.verificar_posicion_disponible(pos_fin) == False:
                raise MovimientoInvalido("No se puede realizar ese movimiento++++")
            self.verificar_movimientos_y_dados(pos_inic,pos_fin)
            self.ocupar_casilla(pos_inic,pos_fin)
        if self.verificar_ganador_y_perdedor() == True:
            raise Ganador("Ganaste!")
        self.verificar_cambio_turno()
    
    def realizar_moviento_desde_inicio(self,pos_fin):
        if self.verificar_posicion_disponible(pos_fin) == False:
            raise MovimientoInvalido("No se puede realizar ese movimiento+++")
        if self.__turno__ == "Blanco":
            pos_inic =-1
        else:
            pos_inic = 24
        self.verificar_movimientos_y_dados(pos_inic,pos_fin)
        board = self.__board__.__contenedor_fichas__
        if len(board[pos_fin]) == 1:
            if board[pos_fin][0].obtener_color() != self.__turno__:
                self.__board__.comer_ficha(pos_fin,self.__turno__)
        self.__board__.quitar_ficha_comida(self.__turno__)
        self.__board__.poner_ficha(pos_fin,self.__turno__)
        self.verificar_cambio_turno()                                                                    


    def ocupar_casilla(self,pos_inic,pos_fin):
        '''Entradas: cuadrante inicial, posición inicial,cuadrante final, posición final y turno actual

        Funcionalidad: Utiliza las funciones quitar_ficha y poner_ficha para hacer el movimiento de la ficha de una casilla a otra
        '''

        board = self.__board__.__contenedor_fichas__

        self.__board__.quitar_ficha(pos_inic)
        if len(board[pos_fin]) == 1:
            if board[pos_fin][0].obtener_color() != self.__turno__:
                self.__board__.comer_ficha(pos_fin,self.__turno__)
        self.__board__.poner_ficha(pos_fin,self.__turno__)

   
    def tirar_dados(self):
        """
        Mantiene interfaz original - usa DiceManager pero sincroniza __dados_disponibles__
        """
        self.__dice_manager__.tirar_dados()
            
        # Sincronizar con __dados_disponibles__ para compatibilidad
        if self.__dice_1__.obtener_numero() == self.__dice_2__.obtener_numero():
            self.__dados_disponibles__ = [self.__dice_1__, self.__dice_1__, 
                                            self.__dice_1__, self.__dice_1__]
        else:
            self.__dados_disponibles__ = [self.__dice_1__, self.__dice_2__]

    def obtener_dados_disponibles(self):
    # Mantener interfaz - delega en DiceManager
        return self.__dice_manager__.obtener_dados_disponibles()
        

    def verificar_posicion_disponible(self, posicion):
        # Mantener para compatibilidad - delega en MoveValidator
        return self.__move_validator__.es_posicion_disponible(
            self.__board__, 
            posicion, 
            self.__turno__
    )

    def verificar_sacar_ficha(self, posicion, board):
        # Mantener para compatibilidad - delega en RuleValidator
        try:
            self.__rule_validator__.puede_sacar_ficha(
                self.__board__, 
                posicion, 
                self.__turno__, 
                self.__dice_1__, 
                self.__dice_2__
            )
            return True
        except ValueError as e:
            raise MovimientoInvalido(str(e))
    
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
    

            if len(board[pos_origen]) == 0:
                return False
            
            if pos_destino < 0 or pos_destino >= 24:
                try:
                    if self.verificar_sacar_ficha(pos_origen, self.__board__.obtener_contenedor_fichas()) == True:
                        return True
                except MovimientoInvalido:
                    pass  
                return False
            
        
            if board[pos_origen][0].obtener_color() != self.__turno__:
                return False
        
            # Usar la función existente para verificar posición destino
                         
            return self.verificar_posicion_disponible(pos_destino)
        #funcion auxiliar para verificar si un movimiento es valido si se saca una ficha que se ha comido
        def es_movimiento_valido_desde_inicio(pos_origen, pasos):
            
                # Calcular destino según el color
            if self.__turno__ == "Blanco":
                pos_destino = pos_origen + pasos  # Blancas van hacia arriba (0->23)
            else:  # Negro
                pos_destino = pos_origen - pasos  # Negras van hacia abajo (23->0)
    
            # Verificar límites
            if pos_destino < 0 or pos_destino >= 24:
                return False
        
            # Usar la función existente para verificar posición destino
            return self.verificar_posicion_disponible(pos_destino)
        if self.obtener_board().verificar_ficha_comida(self.__turno__) == True:
            if self.__turno__ == "Blanco":
                origen = -1
            else:
                origen = 24
            if es_movimiento_valido_desde_inicio(origen, d1.obtener_numero()) or es_movimiento_valido_desde_inicio(origen, d2.obtener_numero()):
                    return True
            if es_movimiento_valido_desde_inicio(origen, d1.obtener_numero() + d2.obtener_numero()):
                    return True
            # Verificar movimientos posibles con cada dado individualmente
        for i in range(24): #falta verifcar que hallan moviemientos desde inicio
                if es_movimiento_valido(i, d1.obtener_numero()) or es_movimiento_valido(i, d2.obtener_numero()):
                    return True
    
        # Verificar movimiento combinado (solo si no son dobles)
        if d1.obtener_numero() != d2.obtener_numero():
            for i in range(24):
                if es_movimiento_valido(i, d1.obtener_numero() + d2.obtener_numero()):
                    return True
    
        # Si no hay movimientos posibles, lanzar excepción
        raise NoHayMovimientosPosibles("No hay movimientos posibles")
    
    def verificar_movimientos_y_dados(self, pos_inic, pos_fin):
        """
        MÉTODO PÚBLICO - Se mantiene para compatibilidad con CLI y tests
        Ahora delega en DiceManager internamente
        """
        # Calcular pasos según el turno
        if self.__turno__ == "Blanco":
            pasos = pos_fin - pos_inic
        else:
            pasos = pos_inic - pos_fin
        
        # Intentar usar dado individual
        try:
            self.__dice_manager__.usar_dado(pasos)
            # Sincronizar con __dados_disponibles__ (compatibilidad)
            if self.__dice_1__.obtener_numero() == pasos and self.__dice_1__ in self.__dados_disponibles__:
                self.__dados_disponibles__.remove(self.__dice_1__)
            elif self.__dice_2__.obtener_numero() == pasos and self.__dice_2__ in self.__dados_disponibles__:
                self.__dados_disponibles__.remove(self.__dice_2__)
            return True
        except ValueError:
            pass
        
        # Intentar usar dados combinados
        try:
            self.__dice_manager__.usar_dados_combinados(pasos)
            # Sincronizar con __dados_disponibles__
            if self.__dice_1__ in self.__dados_disponibles__:
                self.__dados_disponibles__.remove(self.__dice_1__)
            if self.__dice_1__.obtener_numero() == self.__dice_2__.obtener_numero():
                if self.__dice_1__ in self.__dados_disponibles__:
                    self.__dados_disponibles__.remove(self.__dice_1__)
            else:
                if self.__dice_2__ in self.__dados_disponibles__:
                    self.__dados_disponibles__.remove(self.__dice_2__)
            return True
        except ValueError as e:
            raise MovimientoInvalido(e)
            
        
    def verificar_cambio_turno(self):
        '''
        Funcionalidad: Cambiar de turno si no quedan dados en la lista dados disponibles

        Salida: si siguen quedando dados disponibles se mantendrá el turno, si no quedan retornará True
        '''
        if self.__dados_disponibles__ == []:
            self.cambiar_turno()
        else:
            return True
    
    def cambiar_turno(self): #cuando el CLI llame a verificar_movimietos_posibles, si no hay se debe llamar a esta funcion
        if self.__turno__ == 'Blanco':
                self.__turno__ = 'Negro'
        else:
                self.__turno__ = 'Blanco'
    
    def verificar_ganador_y_perdedor(self):
        if self.__board__.verficar_fichas_sacadas_15(self.__turno__) == True:
            if self.__turno__ == "Blanco":
                self.__players__[self.__turno__].definir_ganador()
                self.__players__["Negro"].definir_perdedor()
                return True
            else:
                self.__players__[self.__turno__].definir_ganador()
                self.__players__["Blanco"].definir_perdedor()
                return True
    
    def inicializar_board(self):
        self.__board__.inicializar_tablero()
    