"""
Módulo principal del juego Backgammon.
Contiene la clase BackgammonGame que orquesta la lógica del juego.
"""
from core.board import Board
from core.models.dice import Dice
from core.models.player import Player
from core.services.dice_manager import DiceManager
from core.services.move_calculator import MoveCalculator
from core.validators.move_validator import MoveValidator
from core.validators.rule_validator import RuleValidator

class NoHayMovimientosPosibles(Exception):
    """Excepción lanzada cuando no hay movimientos posibles."""
class MovimientoInvalido(Exception):
    """Excepción lanzada cuando el movimiento que se quiere realizar es inválido."""
class Ganador(Exception):
    """Excepción lanzada cuando hay un ganador."""

class BackgammonGame:
    """
    Clase principal que orquesta el juego de Backgammon.
    Cumple con principios SOLID delegando responsabilidades.
    """
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
        Funcionalidad: Crear una instacia de la clase jugador y agregarla en el diccionario
        '''

        jugador = Player(nom,ficha,estado)
        self.__players__[ficha] = jugador

    def obtener_players(self):
        """Salida: diccionario de jugadores."""
        return self.__players__

    def obtener_turno(self):
        """Salida: turno."""
        return self.__turno__

    def obtener_board(self):
        """Salida: la intancia de tablero utilizada por la clae BackgammonGame"""
        return self.__board__

    def realizar_movimiento(self,pos_inic,pos_fin):
        """
        Entradas: posición inicial y posición final
        Funcionalidad: realizar un moviento despuesde de haber pasado 
                        por la validaciones necesarias
        """
        board = self.__board__.obtener_contenedor_fichas()
        if (len(board[pos_inic]) == 0) or (board[pos_inic][0].obtener_color() != self.__turno__):
            raise MovimientoInvalido("No se puede realizar ese moviemto")
        if pos_fin in (-1,24):
            self.verificar_sacar_ficha(pos_inic,self.__board__)
            self.__board__.sacar_ficha(pos_inic,self.__turno__)
        else:
            if not self.verificar_posicion_disponible(pos_fin):
                raise MovimientoInvalido("No se puede realizar ese movimiento")
            self.verificar_movimientos_y_dados(pos_inic,pos_fin)
            self.ocupar_casilla(pos_inic,pos_fin)
        if self.verificar_ganador_y_perdedor():
            raise Ganador("Ganaste!")
        self.verificar_cambio_turno()

    def realizar_moviento_desde_inicio(self,pos_fin):
        """
        Entradas: posición inicial
        Funcionalidad: realizar un moviento desde inicio despues de de haber 
                        pasado por la validaciones necesarias
        """
        if not self.verificar_posicion_disponible(pos_fin):
            raise MovimientoInvalido("No se puede realizar ese movimiento")
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
        Funcionalidad: Utiliza las funciones quitar_ficha y poner_ficha para 
                    hacer el movimiento de la ficha de una casilla a otra
        '''

        board = self.__board__.__contenedor_fichas__

        self.__board__.quitar_ficha(pos_inic)
        if len(board[pos_fin]) == 1:
            if board[pos_fin][0].obtener_color() != self.__turno__:
                self.__board__.comer_ficha(pos_fin,self.__turno__)
        self.__board__.poner_ficha(pos_fin,self.__turno__)


    def tirar_dados(self):
        """
        Funcionalidad: utiliza a dice_manager para tirar los dados
        """
        self.__dice_manager__.tirar_dados()


    def obtener_dados_disponibles(self):
        """Salida: lista de los dados disponibels"""
        return self.__dice_manager__.obtener_dados_disponibles()


    def verificar_posicion_disponible(self, posicion):
        """
        Entrada: posición
        Funcionalidad: verifica si una posición está diponible utilizando a move validator
        Salida: True o False
        """
        return self.__move_validator__.es_posicion_disponible(
            self.__board__,
            posicion,
            self.__turno__
    )

    def verificar_sacar_ficha(self, posicion, board):
        """
        Entradas: posicion y board board
        Funcionalidad: verifica si se puede sacar una ficha del tablero utilizando a rule_validator
        Salida: True o Excepción MovimientoInvalido si se intenta sacar ficha y no es posible
        """
        try:
            self.__rule_validator__.puede_sacar_ficha(
                board,
                posicion,
                self.__turno__,
                self.__dice_1__,
                self.__dice_2__
            )
            return True
        except ValueError as e:
            raise MovimientoInvalido(str(e)) from e

    def verifificar_movimientos_posibles(self):
        """
        Funcionalidad: utiliza a move_calculator para verificar si hay mivientos posibles
        Salida: True si hay movientos posibles y excepcion NoHayMovimientosPosibles si no los aht
        """
        try:
            return self.__move_calculator__.hay_movimientos_posibles(
                self.__board__,
                self.__turno__,
                self.__dice_manager__
            )
        except ValueError as e:
            raise NoHayMovimientosPosibles(str(e)) from e

    def verificar_movimientos_y_dados(self, pos_inic, pos_fin):
        """
        Entradas: posicion inicial y posicion final
        Funcionalidad: verifica si el movimiento que se quiere realizar coincide con los dados o no
        Salida: True si es valido o Excepcion MovielntoInvalido 
                si el movimiento no coincide con el dado 
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
            raise MovimientoInvalido(str(e)) from e


    def verificar_cambio_turno(self):
        '''
        Funcionalidad: Cambiar de turno si no quedan dados en la lista dados disponibles
        Salida: si siguen quedando dados disponibles se mantendrá el turno, 
                si no quedan retornará True
        '''
        if self.__dice_manager__.obtener_dados_disponibles() == []:
            self.cambiar_turno()
            return None
        return True

    def cambiar_turno(self):
        """
        Funcionalidad: Cambiar de turno según el tueno alctual
        """
        if self.__turno__ == 'Blanco':
            self.__turno__ = 'Negro'
        else:
            self.__turno__ = 'Blanco'

    def verificar_ganador_y_perdedor(self):
        """
        Funcionalidad: verifica si hay ganador, si ese es el caso lo define como ganador
        Salida: True si hubo ganador
        """
        if self.__board__.verficar_fichas_sacadas_15(self.__turno__):
            if self.__turno__ == "Blanco":
                self.__players__[self.__turno__].definir_ganador()
                self.__players__["Negro"].definir_perdedor()
            else:
                self.__players__[self.__turno__].definir_ganador()
                self.__players__["Blanco"].definir_perdedor()
            return True

    def inicializar_board(self):
        """
        Funcionalidad: Define el estado inicial del tablero segun las reglas del juego
        """
        self.__board__.inicializar_tablero()
