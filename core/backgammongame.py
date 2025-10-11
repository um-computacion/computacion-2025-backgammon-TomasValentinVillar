from core.board import Board
from core.models.dice import Dice
from core.models.player import Player
from core.services.dice_manager import DiceManager
from core.services.move_calculator import MoveCalculator
from core.validators.move_validator import MoveValidator
from core.validators.rule_validator import RuleValidator

class NoHayMovimientosPosibles(Exception):
    pass
class MovimientoInvalido(Exception):
    pass
class Ganador(Exception):
    pass

class BackgammonGame:
    def __init__(self, board=None, dice1=None, dice2=None, 
                 move_validator=None, rule_validator=None):
        self.__turno__ = "Blanco"
        
        # Inyección de dependencias
        self.__board__ = board if board is not None else Board()
        self.__dice_1__ = dice1 if dice1 is not None else Dice()
        self.__dice_2__ = dice2 if dice2 is not None else Dice()
        
        self.__move_validator__ = move_validator if move_validator is not None else MoveValidator()
        self.__rule_validator__ = rule_validator if rule_validator is not None else RuleValidator()
        self.__dice_manager__ = DiceManager(self.__dice_1__, self.__dice_2__)
        self.__move_calculator__ = MoveCalculator(
            self.__move_validator__, 
            self.__rule_validator__
        )
        self.__players__ = {}
    
    
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
        '''Entradas: posición inicial y posición final

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
            

    def obtener_dados_disponibles(self):
        """LEGACY - Mantiene interfaz para compatibilidad"""
        return self.__dice_manager__.obtener_dados_disponibles()
        

    def verificar_posicion_disponible(self, posicion):
        # LEGACY Mantener para compatibilidad - delega en MoveValidator
        return self.__move_validator__.es_posicion_disponible(
            self.__board__, 
            posicion, 
            self.__turno__
    )

    def verificar_sacar_ficha(self, posicion, board):
        # LEGACY Mantener para compatibilidad - delega en RuleValidator
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
        # Mantener interfaz - delega en MoveCalculator
        try:
            return self.__move_calculator__.hay_movimientos_posibles(
                self.__board__, 
                self.__turno__, 
                self.__dice_manager__
            )
        except ValueError as e:
            raise NoHayMovimientosPosibles(str(e))
    
    def verificar_movimientos_y_dados(self, pos_inic, pos_fin):
        """
        LEGACY MÉTODO PÚBLICO - Se mantiene para compatibilidad con CLI y tests
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
            return True
        except ValueError:
            pass
        
        # Intentar usar dados combinados
        try:
            self.__dice_manager__.usar_dados_combinados(pasos)
            return True
        except ValueError as e:
            raise MovimientoInvalido(str(e))
            
        
    def verificar_cambio_turno(self):
        '''
        Funcionalidad: Cambiar de turno si no quedan dados en la lista dados disponibles

        Salida: si siguen quedando dados disponibles se mantendrá el turno, si no quedan retornará True
        '''
        if self.__dice_manager__.obtener_dados_disponibles() == []:
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
    