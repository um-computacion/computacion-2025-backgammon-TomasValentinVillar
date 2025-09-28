from core.checker import Checker

class Board:
    def __init__(self):
        self.__contenedor_fichas__ = [
            [],[],[],[],[],[], [],[],[],[],[],[],
            [],[],[],[],[],[], [],[],[],[],[],[]
        ]
        self.__contenedor_fichas_blancas_sacadas__ = []
        self.__contenedor_fichas_negras_sacadas__ = []
        self.__contenedor_fichas_blancas__ = []
        self.__contenedor_fichas_negras__ = []

    
    '''Entradas: cuadrante, posición y turno actual

        Funcionalidad: Quita una ficha en una posición especifica de un cuadrante, restádole 1 a la posición y definiendo el color
    '''
    def quitar_ficha(self,pos):
        self.__contenedor_fichas__[pos].pop()  
    
    def poner_ficha(self, pos, turno):

        self.__contenedor_fichas__[pos].append(Checker(turno))
    
    def obtener_contenedor_fichas(self):
        return self.__contenedor_fichas__
    
    def obtener_contenedor_blancas(self):
        return self.__contenedor_fichas_blancas__
    
    def obtener_contenedor_negras(self):
        return self.__contenedor_fichas_negras__
    
    def obtener_contenedor_blancas_sacadas(self):
        return self.__contenedor_fichas_blancas_sacadas__

    def obtener_contenedor_negras_sacadas(self):
        return self.__contenedor_fichas_negras_sacadas__

    def comer_ficha(self,pos_fin,turno):
        '''Entradas: Posicion final y turno

        Funcionalidad: quitar la fucha de la posición indicada y agregar la ficha correspondiente al turno contrario al
                        contenenedor correspondiente a las fichas que se han comido 
        '''
        self.__contenedor_fichas__[pos_fin].pop()
        if turno == "Blanco":
            self.__contenedor_fichas_negras__.append(Checker("Negro"))
        else:
            self.__contenedor_fichas_blancas__.append(Checker("Blanco"))
    
    def sacar_ficha(self,pos_inic,turno):
        '''Entradas: Posicion final y turno

        Funcionalidad: quitar la fucha de la posición indicada y agregar la ficha correspondiente al turno contrario al
                        contenenedor correspondiente a las fichas que se han sacado
        '''
        self.__contenedor_fichas__[pos_inic].pop()
        if turno == "Blanco":
            self.__contenedor_fichas_blancas_sacadas__.append(Checker("Blanco"))
        else:
            self.__contenedor_fichas_negras_sacadas__.append(Checker("Negro"))
    
    def verficar_fichas_sacadas_15(self,turno):
        """
        Entradas: turno

        Funcion: verificar si las fichas que se han sacado son 15 para saber si el tunrno correspondiente ha ganado la partida
        """
        if turno == "Blanco":
            if len(self.__contenedor_fichas_blancas_sacadas__ ) == 15:
                return True
        else:
            if len(self.__contenedor_fichas_negras_sacadas__ ) == 15:
                return True
    
    def quitar_ficha_comida(self,turno):
        if turno == "Blanco":
            self.__contenedor_fichas_blancas__.pop()
        else:
            self.__contenedor_fichas_negras__.pop()
    

    def _get_piece_symbol(self, checker):
        """
        Obtiene el símbolo visual de una ficha
        Args: checker - objeto Checker
        Returns: 'W' para blancas, 'B' para negras
        """
        return 'W' if checker.obtener_color() == 'Blanco' else 'B'

    def draw_full_board(self):
        """
        Genera una representación visual del tablero para las interfaces
        Retorna: Lista de listas representando el tablero visualmente
        - Muestra las 24 posiciones (0-23) del tablero
        - 5 filas máximo por columna
        - Si hay más de 5 fichas, muestra el número en la fila 
        """
        result_board = []
        for row in range(0,5):
            result_row = []
            for col in range(11, -1, -1):
                position_pieces = self.__contenedor_fichas__[col]
                if len(position_pieces) > 0:
                    if len(position_pieces) > row:
                        if row < 4:
                            piece = self._get_piece_symbol(position_pieces[0])
                        else:
                            if len(position_pieces) <= 5:
                                piece = self._get_piece_symbol(position_pieces[0])
                            else:
                                piece = str(len(position_pieces) - 4)
                        result_row.append(piece)
                    else:
                        result_row.append(' ')
                else:
                    result_row.append(' ')
            result_board.append(result_row)
        
        
        # Segunda mitad: posiciones 12 a 23
        for row in range(0,5):
            result_row = []
                        
            for col in range(12, 24):
                position_pieces = self.__contenedor_fichas__[col]
                if len(position_pieces) > 0:
                    if len(position_pieces) > row:
                        if row < 4:
                            piece = self._get_piece_symbol(position_pieces[0])
                        else:
                            if len(position_pieces) <= 5:
                                piece = self._get_piece_symbol(position_pieces[0])
                            else:
                                piece = str(len(position_pieces) - 4)
                        result_row.append(piece)
                    else:
                        result_row.append(' ')
                else:
                    result_row.append(' ')
            result_board.append(result_row)
                    
        return result_board