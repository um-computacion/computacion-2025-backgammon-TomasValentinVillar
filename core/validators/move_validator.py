

class MoveValidator:
    """
    Responsabilidad: Validar si un movimiento es legal según las reglas básicas
    Cumple con SRP: Solo valida movimientos
    """
    
    def es_posicion_disponible(self, board, posicion, turno):
        """
        Verifica si una posición está disponible para colocar una ficha
        
        Args:
            board: Instancia de Board
            posicion: int - posición a verificar (0-23)
            turno: str - "Blanco" o "Negro"
            
        Returns:
            bool - True si la posición está disponible
        """
        contenedor = board.obtener_contenedor_fichas()
        
        # Posición vacía
        if len(contenedor[posicion]) == 0:
            return True
        
        # Posición con fichas del mismo color
        if contenedor[posicion][0].obtener_color() == turno:
            return True
        
        # Posición con solo 1 ficha enemiga (se puede comer)
        if len(contenedor[posicion]) == 1:
            return True
        
        # Posición bloqueada (2+ fichas enemigas)
        return False
    
    def validar_movimiento_basico(self, board, pos_inicial, turno):
        """
        Valida que la posición inicial tenga una ficha del turno actual
        
        Args:
            board: Instancia de Board
            pos_inicial: int - posición inicial
            turno: str - turno actual
            
        Returns:
            bool - True si es válido
            
        Raises:
            ValueError si el movimiento no es válido
        """
        contenedor = board.obtener_contenedor_fichas()
        
        # Verificar que haya fichas en la posición inicial
        if len(contenedor[pos_inicial]) == 0:
            raise ValueError("No hay fichas en la posición inicial")
        
        # Verificar que la ficha sea del color correcto
        if contenedor[pos_inicial][0].obtener_color() != turno:
            raise ValueError("La ficha no es del turno actual")
        
        return True
    
    def calcular_destino(self, pos_inicial, pasos, turno):
        """
        Calcula la posición destino según el turno
        
        Args:
            pos_inicial: int - posición inicial
            pasos: int - número de pasos del dado
            turno: str - turno actual
            
        Returns:
            int - posición destino
        """
        if turno == "Blanco":
            return pos_inicial + pasos  # Blancas van hacia arriba (0->23)
        else:  # Negro
            return pos_inicial - pasos  # Negras van hacia abajo (23->0)
    
    def es_posicion_valida(self, posicion):
        """
        Verifica si una posición está dentro del tablero
        
        Args:
            posicion: int - posición a verificar
            
        Returns:
            bool - True si está en rango 0-23
        """
        return 0 <= posicion < 24