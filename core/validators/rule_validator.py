# core/validators/rule_validator.py

class RuleValidator:
    """
    Responsabilidad: Validar reglas especiales del Backgammon
    Cumple con SRP: Solo valida reglas del juego
    """
    
    def puede_sacar_ficha(self, board, posicion, turno, dado1, dado2):
        """
        Verifica si se puede sacar una ficha del tablero
        
        Reglas:
        - Todas las fichas deben estar en el home board
        - El movimiento debe coincidir con un dado o ser menor si no hay fichas más atrás
        
        Args:
            board: Instancia de Board
            posicion: int - posición de la ficha a sacar
            turno: str - turno actual
            dado1, dado2: Instancias de Dice
            
        Returns:
            bool - True si se puede sacar
            
        Raises:
            ValueError si no se puede sacar
        """
        contenedor = board.obtener_contenedor_fichas()
        
        if turno == "Blanco":
            return self._puede_sacar_ficha_blanca(contenedor, posicion, dado1, dado2)
        else:
            return self._puede_sacar_ficha_negra(contenedor, posicion, dado1, dado2)
    
    def _puede_sacar_ficha_blanca(self, contenedor, posicion, dado1, dado2):
        """
        Verifica si las blancas pueden sacar ficha
        Home board: posiciones 18-23
        """
        # Verificar que no hay fichas blancas fuera del home board (0-17)
        for pos in range(18):
            if len(contenedor[pos]) > 0:
                if contenedor[pos][0].obtener_color() == "Blanco":
                    raise ValueError("No se puede sacar ficha: hay fichas fuera del home board")
        
        # Calcular distancia al final
        distancia = 24 - posicion
        
        # Verificar si coincide con algún dado
        if distancia <= dado1.obtener_numero() or distancia <= dado2.obtener_numero():
            return True
        
        raise ValueError("El movimiento no coincide con ningún dado")
    
    def _puede_sacar_ficha_negra(self, contenedor, posicion, dado1, dado2):
        """
        Verifica si las negras pueden sacar ficha
        Home board: posiciones 0-5
        """
        # Verificar que no hay fichas negras fuera del home board (6-23)
        for pos in range(6, 24):
            if len(contenedor[pos]) > 0:
                if contenedor[pos][0].obtener_color() == "Negro":
                    raise ValueError("No se puede sacar ficha: hay fichas fuera del home board")
        
        # Calcular distancia al final
        distancia = posicion + 1
        
        # Verificar si coincide con algún dado
        if distancia <= dado1.obtener_numero() or distancia <= dado2.obtener_numero():
            return True
        
        raise ValueError("El movimiento no coincide con ningún dado")
    
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
        else:
            # Home board negras: 0-5
            for pos in range(6, 24):
                if len(contenedor[pos]) > 0:
                    if contenedor[pos][0].obtener_color() == "Negro":
                        return False
            return True