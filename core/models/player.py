'''
Modulo encargado de los jugadores
contiene a la clase Player
'''

class Player:
    '''
    Respnsabilidad: Representa a los jugadores de Backgammon
    '''
    def __init__(self,nombre,ficha,estado):
        self.__nombre__ = nombre
        self.__ficha__ = ficha
        self.__estado__ = estado

    def obtener_nombre(self):
        '''
        Funcionalidad: Retorna el atributo nombre de los jugadores
        '''
        return self.__nombre__

    def obtener_ficha(self):
        '''
        Funcionalidad: Retorna el atributo ficha
        '''
        return self.__ficha__

    def obtener_estado(self):
        '''
        Funcionalidad: Retorna el atributo estado
        '''
        return self.__estado__

    def definir_ganador(self):
        '''
        Funcionalidad: Define el estado Ganador del jugador 
        '''
        self.__estado__ = "Ganador"

    def definir_perdedor(self):
        '''
        Funcionalidad: Define el estado Perdedor del jugador 
        '''
        self.__estado__ = "Perdedor"
