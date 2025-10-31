"""
Modulo encargado de calcular movimientos
contiene a la clase MoveCalculator
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

        # Obtener TODOS los dados disponibles
        dados_disponibles = dice_manager.obtener_dados_disponibles()

        if not dados_disponibles:
            return False

        # Verificar cada dado disponible individualmente
        valores_vistos = set()

        for dado in dados_disponibles:
            valor = dado.obtener_numero()

            if valor in valores_vistos:
                continue
            valores_vistos.add(valor)

            pos_destino = self.__move_validator__.calcular_destino(pos_inicio, valor, turno)

            if self.__move_validator__.es_posicion_valida(pos_destino):
                if self.__move_validator__.es_posicion_disponible(board, pos_destino, turno):
                    return True

        return False

    def _hay_movimientos_normales(self, board, turno, dice_manager):
        """
        Verifica si hay movimientos normales posibles
        """
        contenedor = board.obtener_contenedor_fichas()
        dados_disponibles = dice_manager.obtener_dados_disponibles()

        if not dados_disponibles:
            return False

        # Obtener valores únicos de dados disponibles
        valores_unicos = set(d.obtener_numero() for d in dados_disponibles)

        # Verificar cada posición del tablero
        for pos in range(24):
            if len(contenedor[pos]) == 0:
                continue

            if contenedor[pos][0].obtener_color() != turno:
                continue

            # Probar movimiento con cada dado disponible
            for valor in valores_unicos:
                if self._es_movimiento_valido(board, pos, valor, turno, dice_manager):
                    return True

        return False

    def _es_movimiento_valido(self, board, pos_origen, pasos, turno, dice_manager):
        """
        Verifica si un movimiento específico es válido
        """
        pos_destino = self.__move_validator__.calcular_destino(pos_origen, pasos, turno)

        if not self.__move_validator__.es_posicion_valida(pos_destino):
            # Verificar si puede sacar ficha
            try:
                dados_disponibles = dice_manager.obtener_dados_disponibles()
                self.__rule_validator__.puede_sacar_ficha(
                    board,
                    pos_origen,
                    turno,
                    dados_disponibles
                )
                return True
            except ValueError:
                return False
        if (turno == "Blanco" and pos_destino == 23) or (turno == "Negro" and pos_destino == 0):
            # Verificar si TODAS las fichas están en home board
            if self.__rule_validator__.todas_fichas_en_home_board(board, turno):
                # Verificar si el dado coincide EXACTAMENTE para sacar
                try:
                    dados_disponibles = dice_manager.obtener_dados_disponibles()
                    self.__rule_validator__.puede_sacar_ficha(
                        board,
                        pos_origen,
                        turno,
                        dados_disponibles
                    )
                    return True  # Puede sacar desde pos 23/0
                except ValueError:
                    pass  # No puede sacar, intentar movimiento normal

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
