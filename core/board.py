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