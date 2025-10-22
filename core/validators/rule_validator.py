"""
Modulo encargado validar reglas especiales del Backgammon
Contiene a la clase RuleValidator
"""

class RuleValidator:
    """
    Responsabilidad: Validar reglas especiales del Backgammon
    Cumple con SRP: Solo valida reglas del juego
    """

    def puede_sacar_ficha(self, board, posicion, turno, dados_disponibles):
        """
        Verifica si se puede sacar una ficha del tablero

        Reglas CORRECTAS:
        - Todas las fichas deben estar en el home board
        - El dado debe coincidir EXACTAMENTE con la distancia, O
        - Si el dado es MAYOR y NO hay fichas más atrás, se puede sacar

        Args:
            board: Instancia de Board
            posicion: int - posición de la ficha a sacar
            turno: str - turno actual
            dados_disponibles: list - Lista de instancias de Dice DISPONIBLES

        Returns:
            int - El dado que se debe usar (para consumirlo después)

        Raises:
            ValueError si no se puede sacar
        """
        contenedor = board.obtener_contenedor_fichas()

        # Extraer valores de dados DISPONIBLES
        valores_disponibles = [d.obtener_numero() for d in dados_disponibles]

        if turno == "Blanco":
            return self._puede_sacar_ficha_blanca(contenedor, posicion, valores_disponibles)
        return self._puede_sacar_ficha_negra(contenedor, posicion, valores_disponibles)

    def _puede_sacar_ficha_blanca(self, contenedor, posicion, valores_disponibles):
        """
        Verifica si las blancas pueden sacar ficha
        Home board: posiciones 18-23
        """
        # Verificar que no hay fichas blancas fuera del home board (0-17)
        for pos in range(18):
            if len(contenedor[pos]) > 0:
                if contenedor[pos][0].obtener_color() == "Blanco":
                    raise ValueError("No se puede sacar ficha: hay fichas fuera del home board")

        # Calcular distancia exacta al final
        distancia = 24 - posicion

        # Buscar dado EXACTO disponible
        if distancia in valores_disponibles:
            return distancia

        # Buscar dado MAYOR (solo si NO hay fichas más atrás)
        # Verificar que no hay fichas blancas en posiciones anteriores (18 a posicion-1)
        hay_fichas_atras = False
        for pos in range(18, posicion):
            if len(contenedor[pos]) > 0:
                if contenedor[pos][0].obtener_color() == "Blanco":
                    hay_fichas_atras = True
                    break

        if not hay_fichas_atras:
            # Buscar el dado disponible más pequeño que sea mayor a la distancia
            dados_mayores = [v for v in valores_disponibles if v > distancia]
            if dados_mayores:
                return min(dados_mayores)  # Retornar el más pequeño

        raise ValueError("No se puede sacar: el dado no coincide con la distancia")

    def _puede_sacar_ficha_negra(self, contenedor, posicion, valores_disponibles):
        """
        Verifica si las negras pueden sacar ficha
        Home board: posiciones 0-5
        """
        # Verificar que no hay fichas negras fuera del home board (6-23)
        for pos in range(6, 24):
            if len(contenedor[pos]) > 0:
                if contenedor[pos][0].obtener_color() == "Negro":
                    raise ValueError("No se puede sacar ficha: hay fichas fuera del home board")

        # Calcular distancia exacta al final
        distancia = posicion + 1

        #Buscar dado EXACTO disponible
        if distancia in valores_disponibles:
            return distancia

        # Buscar dado MAYOR (solo si NO hay fichas más atrás)
        # Verificar que no hay fichas negras en posiciones posteriores (posicion+1 a 5)
        hay_fichas_atras = False
        for pos in range(posicion + 1, 6):
            if len(contenedor[pos]) > 0:
                if contenedor[pos][0].obtener_color() == "Negro":
                    hay_fichas_atras = True
                    break

        if not hay_fichas_atras:
            # Buscar el dado disponible más pequeño que sea mayor a la distancia
            dados_mayores = [v for v in valores_disponibles if v > distancia]
            if dados_mayores:
                return min(dados_mayores)  # Retornar el más pequeño

        raise ValueError("No se puede sacar: el dado no coincide con la distancia")

    def tiene_fichas_comidas(self, board, turno):
        """
        Verifica si un jugador tiene fichas comidas que debe volver a meter
        
        Args:
            board: Instancia de Board
            turno: str - turno actual
            
        Returns:
            bool - True si hay fichas comidas
        """
        return board.verificar_ficha_comida(turno)

    def todas_fichas_en_home_board(self, board, turno):
        """
        Verifica si todas las fichas están en el home board
        (necesario para poder empezar a sacar fichas)

        Args:
            board: Instancia de Board
            turno: str - turno actual

        Returns:
            bool - True si todas están en home board
        """
        contenedor = board.obtener_contenedor_fichas()

        if turno == "Blanco":
            # Home board blancas: 18-23
            for pos in range(18):
                if len(contenedor[pos]) > 0:
                    if contenedor[pos][0].obtener_color() == "Blanco":
                        return False
            return True
        # Home board negras: 0-5
        for pos in range(6, 24):
            if len(contenedor[pos]) > 0:
                if contenedor[pos][0].obtener_color() == "Negro":
                    return False
        return True
