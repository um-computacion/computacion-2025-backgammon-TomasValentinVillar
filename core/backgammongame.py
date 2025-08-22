from core.board import Board
class BackgammonGame:
    def __init__(self):
        self.__turno__ = "B"
        self.__board__ = Board()

    '''Entradas: cuadrante inicial, posición inicial,cuadrante final, posición final y turno actual

        Funcionalidad: Utiliza las funciones quitar_ficha y poner_ficha para hacer el movimiento de la ficha de una casilla a otra
    '''
    def ocupar_casilla(self,cuand_inic, pos_inic,cuad_fin,pos_fin):
        self.__board__.quitar_ficha(cuand_inic,pos_inic,self.__turno__)
        self.__board__.poner_ficha(cuad_fin,pos_fin,self.__turno__)
        if self.__turno__ == 'B':
            self.__turno__ = 'N'
        else:
            self.__turno__ = 'N'