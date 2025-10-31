# ui/board_adapter.py
"""
Adaptador entre BackgammonGame y el renderizador pygame.
Convierte la estructura de Checkers a tuplas (color, cantidad).
"""

class BoardAdapter:
    """
    Simula la estructura game.board.pos que espera render_board().
    """
    
    def __init__(self, backgammon_game):
        self.__backgammon_game__ = backgammon_game
        self.__pos__ = {}
        self.actualizar()
    
    def actualizar(self):
        """
        Sincroniza self.pos con el estado actual de BackgammonGame.
        Convierte: [Checker, Checker, ...] → ('white'/'black', cantidad)
        """
        contenedor = self.__backgammon_game__.obtener_board().obtener_contenedor_fichas()
        
        for i in range(24):
            fichas = contenedor[i]
            
            if len(fichas) == 0:
                # Posición vacía
                self.__pos__[i] = None
            else:
                # Obtener color de la primera ficha
                color_checker = fichas[0].obtener_color()
                
                # Convertir a formato pygame
                color_pygame = 'white' if color_checker == 'Blanco' else 'black'
                cantidad = len(fichas)
                
                self.__pos__[i] = (color_pygame, cantidad)