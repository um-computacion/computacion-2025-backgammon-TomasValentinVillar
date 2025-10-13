'''
Modulo encargado de gestionar al tablero de Backgammon
Contiene a clase Board
'''
from core.models.checker import Checker

class Board:
    '''
    Clase que se encarga de gestionar el tabelro de Backgammon
    coniene al tablero principal y las listas que contiene a las
    fichas que se han comido o sacado del tablero, se encarga de
    poner y quitar fichas y de proveer información sobre el tablero
    '''
    def __init__(self):
        self.__contenedor_fichas__ = [
            [],[],[],[],[],[], [],[],[],[],[],[],
            [],[],[],[],[],[], [],[],[],[],[],[]
        ]
        self.__contenedor_fichas_blancas_sacadas__ = []
        self.__contenedor_fichas_negras_sacadas__ = []
        self.__contenedor_fichas_blancas__ = []
        self.__contenedor_fichas_negras__ = []



    def quitar_ficha(self,pos):
        '''Entradas: posición
        Funcionalidad: Quita una ficha en una posición especifica del tablero
        '''
        self.__contenedor_fichas__[pos].pop()

    def poner_ficha(self, pos, turno):
        '''Entradas: posición y turno
        Funcionalidad: Agrega una ficha especifica a una posición, 
        el color de la ficha está definido por el turno
        '''
        self.__contenedor_fichas__[pos].append(Checker(turno))

    def obtener_contenedor_fichas(self):
        '''
        Funcionalidad: Retorna la lista contenedor de fichas (tablero)
        '''
        return self.__contenedor_fichas__

    def obtener_contenedor_blancas(self):
        '''
        Funcionalidad: Retorna la lista contenedor de fichas blancas,
        que es la lista que contiene las fichas blancas que se han comido
        '''
        return self.__contenedor_fichas_blancas__

    def obtener_contenedor_negras(self):
        '''
        Funcionalidad: Retorna la lista contenedor de fichas negras,
        que es la lista que contiene las fichas negras que se han comido
        '''
        return self.__contenedor_fichas_negras__

    def obtener_contenedor_blancas_sacadas(self):
        '''
        Funcionalidad: Retorna la lista contenedor de fichas blancas sacadas,
        que es la lista que contiene las fichas blancas que se han sacado del tablero
        '''
        return self.__contenedor_fichas_blancas_sacadas__

    def obtener_contenedor_negras_sacadas(self):
        '''
        Funcionalidad: Retorna la lista contenedor de fichas negars sacadas,
        que es la lista que contiene las fichas negars que se han sacado del tablero
        '''
        return self.__contenedor_fichas_negras_sacadas__

    def comer_ficha(self,pos_fin,turno):
        '''Entradas: Posicion final y turno

        Funcionalidad: quitar la ficha de la posición indicada y agregar la ficha 
        correspondiente al turno contrario al contenenedor correspondiente a las 
        fichas que se han comido 
        '''
        self.__contenedor_fichas__[pos_fin].pop()
        if turno == "Blanco":
            self.__contenedor_fichas_negras__.append(Checker("Negro"))
        else:
            self.__contenedor_fichas_blancas__.append(Checker("Blanco"))

    def sacar_ficha(self,pos_inic,turno):
        '''Entradas: Posicion final y turno

        Funcionalidad: quitar la fucha de la posición indicada y agregar la ficha correspondiente 
        al turno contrario al contenenedor correspondiente a las fichas que se han sacado
        '''
        self.__contenedor_fichas__[pos_inic].pop()
        if turno == "Blanco":
            self.__contenedor_fichas_blancas_sacadas__.append(Checker("Blanco"))
        else:
            self.__contenedor_fichas_negras_sacadas__.append(Checker("Negro"))

    def verficar_fichas_sacadas_15(self,turno):
        """
        Entradas: turno

        Funcion: verificar si las fichas que se han sacado son 15 para saber 
        si el tunrno correspondiente ha ganado la partida
        """
        if turno == "Blanco":
            if len(self.__contenedor_fichas_blancas_sacadas__ ) == 15:
                return True
        else:
            if len(self.__contenedor_fichas_negras_sacadas__ ) == 15:
                return True
        return None

    def quitar_ficha_comida(self,turno):
        '''
        Entrada: turno
        Funcionalidad: quita la ficha de lista que contiene las fichas que se han comido
        segun el turno correspondiente
        '''
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
        result_board = self.draw_upper_board() + self.draw_lower_board()

        return result_board
    def draw_upper_board(self):
        """
        Genera una representación visual del tablero para los
        cuadrantes de arriba
        Retorna: Lista de listas representando el tablero visualmente
        - Muestra las primeras 12 posiciones (0-11) del tablero
        - 5 filas máximo por columna
        - Si hay más de 5 fichas, muestra el número en la fila
        """
        result_board = []
        for row in range(0, 5):
            result_row = []
            for col in range(11, -1, -1):
                position_pieces = self.__contenedor_fichas__[col]
                piece = self._get_piece_for_position(position_pieces, row)
                result_row.append(piece)
            result_board.append(result_row)
        return result_board

    def _get_piece_for_position(self, position_pieces, row):
        """
        Determina qué mostrar en una posición específica del tablero superior
        """
        if len(position_pieces) == 0:
            return ' '

        if len(position_pieces) <= row:
            return ' '

        if row < 4:
            return self._get_piece_symbol(position_pieces[0])

        # row == 4
        if len(position_pieces) <= 5:
            return self._get_piece_symbol(position_pieces[0])

        return str(len(position_pieces) - 4)

    def draw_lower_board(self):
        """
        Genera una representación visual del tablero para los
        cuadrantes de abajo
        Retorna: Lista de listas representando el tablero visualmente
        - Muestra ultimas 12 posiciones (12-23) del tablero
        - 5 filas máximo por columna
        - Si hay más de 5 fichas, muestra el número en la fila
        """
        result_board = []
        for row in range(0, 5):
            result_row = []
            for col in range(12, 24):
                position_pieces = self.__contenedor_fichas__[col]
                piece = self._get_piece_for_position(position_pieces, row)
                result_row.append(piece)
            result_board.append(result_row)
        return result_board

    def inicializar_tablero(self):
        """
        Funcionalidad: Define el estado inicial del tablero segun las reglas del juego
        """
        self.__contenedor_fichas__[0].extend([
            Checker('Blanco'),Checker('Blanco')])
        self.__contenedor_fichas__[11].extend([
            Checker('Blanco'),Checker('Blanco'),Checker('Blanco'),
            Checker("Blanco"),Checker("Blanco")])
        self.__contenedor_fichas__[16].extend([
            Checker('Blanco'),Checker('Blanco'),Checker('Blanco')])
        self.__contenedor_fichas__[18].extend([
            Checker('Blanco'),Checker('Blanco'),Checker('Blanco'),
            Checker("Blanco"),Checker("Blanco")])
        self.__contenedor_fichas__[23].extend([
            Checker('Negro'),Checker('Negro')])
        self.__contenedor_fichas__[12].extend(
            [Checker('Negro'),Checker('Negro'),Checker('Negro'),
             Checker("Negro"),Checker("Negro")])
        self.__contenedor_fichas__[7].extend([Checker('Negro'),
            Checker('Negro'),Checker('Negro')])
        self.__contenedor_fichas__[5].extend([
            Checker('Negro'),Checker('Negro'),
            Checker('Negro'),Checker("Negro"),Checker("Negro")])

    def verificar_ficha_comida(self,turno):
        '''
        Entradas: turno
        Funcionalidad: verifica si hay alguna ficha que ha sido comida
        para saber si se empieza desde el principio o nó
        Salida: booleano (True o False)
        '''
        if turno == "Blanco":
            if len(self.__contenedor_fichas_blancas__) > 0:
                return True
        else:
            if len(self.__contenedor_fichas_negras__) > 0:
                return True
        return False

    def obtener_cantidad_de_fichas_comidas(self,turno):
        '''
        Entradas: turno
        Funcionalidad: retorna la cantidad de fichas que se almacenan
        en el contenedor de fichas que han sido comidas
        Salida: entero
        '''
        if turno == "Blanco":
            return len(self.obtener_contenedor_blancas())
        return len(self.obtener_contenedor_negras())
