"""
Modulo encargado de calcular movimientos
contiene a la clase Movecalculator
"""

class MoveCalculator:
    """
    Responsabilidad: Calcular movimientos
    Cumple con SRP: Solo calcula movimientos, no los ejecuta
    """

    def __init__(self, move_validator, rule_validator):
        """
        Args:
            move_validator: Instancia de MoveValidator
            rule_validator: Instancia de RuleValidator
        """
        self.__move_validator__ = move_validator
        self.__rule_validator__ = rule_validator

    def hay_movimientos_posibles(self, board, turno, dice_manager):
        """
        Verifica si hay al menos un movimiento posible
    
        Args:
            board: Instancia de Board
            turno: str - turno actual
            dice_manager: Instancia de DiceManager

        Returns:
            bool - True si hay movimientos posibles

        Raises:
            ValueError si no hay movimientos posibles
        """
        # Si hay fichas comidas, solo se pueden mover esas
        if self.__rule_validator__.tiene_fichas_comidas(board, turno):
            if self._hay_movimientos_desde_inicio(board, turno, dice_manager):
                return True
        else:
            # Verificar movimientos normales
            if self._hay_movimientos_normales(board, turno, dice_manager):
                return True

        raise ValueError("No hay movimientos posibles")

    def _hay_movimientos_desde_inicio(self, board, turno, dice_manager):
        """
        Verifica si se puede meter una ficha comida
        """
        # Determinar posición de inicio según el color
        pos_inicio = -1 if turno == "Blanco" else 24

        valores = dice_manager.obtener_valores()
        dado1_val, dado2_val = valores

        # Probar con cada dado individual
        for pasos in [dado1_val, dado2_val]:
            pos_destino = self.__move_validator__.calcular_destino(pos_inicio, pasos, turno)

            if self.__move_validator__.es_posicion_valida(pos_destino):
                if self.__move_validator__.es_posicion_disponible(board, pos_destino, turno):
                    return True

        # Probar con movimiento combinado (si no son dobles)
        if dado1_val != dado2_val:
            pasos_comb = dado1_val + dado2_val
            pos_destino = self.__move_validator__.calcular_destino(pos_inicio, pasos_comb, turno)

            if self.__move_validator__.es_posicion_valida(pos_destino):
                if self.__move_validator__.es_posicion_disponible(board, pos_destino, turno):
                    return True

        return False

    def _hay_movimientos_normales(self, board, turno, dice_manager):
        """
        Verifica si hay movimientos normales posibles
        """
        contenedor = board.obtener_contenedor_fichas()
        valores = dice_manager.obtener_valores()
        dado1_val, dado2_val = valores

        # Verificar cada posición del tablero
        for pos in range(24):
            # Verificar que hay fichas del turno actual
            if len(contenedor[pos]) == 0:
                continue

            if contenedor[pos][0].obtener_color() != turno:
                continue

            # Probar movimiento con dado 1
            if self._es_movimiento_valido(board, pos, dado1_val, turno, dice_manager):
                return True

            # Probar movimiento con dado 2
            if self._es_movimiento_valido(board, pos, dado2_val, turno, dice_manager):
                return True

            # Probar movimiento combinado (si no son dobles)
            if dado1_val != dado2_val:
                pasos_combinados = dado1_val + dado2_val
                if self._es_movimiento_valido(board, pos, pasos_combinados, turno, dice_manager):
                    return True

        return False

    def _es_movimiento_valido(self, board, pos_origen, pasos, turno, dice_manager):
        """
        Verifica si un movimiento específico es válido
        """
        pos_destino = self.__move_validator__.calcular_destino(pos_origen, pasos, turno)

        # Verificar si está sacando ficha
        if not self.__move_validator__.es_posicion_valida(pos_destino):
            try:
                valores = dice_manager.obtener_valores()
                from core.models.dice import Dice
                dado1 = Dice()
                dado2 = Dice()
                dado1.__numero__ = valores[0]
                dado2.__numero__ = valores[1]

                self.__rule_validator__.puede_sacar_ficha(board, pos_origen, turno, dado1, dado2)
                return True
            except ValueError:
                return False

        # Movimiento normal
        return self.__move_validator__.es_posicion_disponible(board, pos_destino, turno)

    def calcular_pasos_movimiento(self, pos_inicial, pos_final, turno):
        """
        Calcula cuántos pasos hay entre dos posiciones

        Args:
            pos_inicial: int - posición inicial
            pos_final: int - posición final
            turno: str - turno actual

        Returns:
            int - número de pasos
        """
        if turno == "Blanco":
            return pos_final - pos_inicial
        return pos_inicial - pos_final
