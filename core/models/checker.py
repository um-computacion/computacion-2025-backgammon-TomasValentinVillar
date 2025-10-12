'''
Modulo encargado de la ficha
contiene a al clase Checker
'''
class Checker:
    '''
    Responsabilidad: Representa una ficha de Backgammon
    '''
    def __init__(self, color : str):
        self.__color__ = color

    def obtener_color(self):
        '''
        Funcionalidad: Retorna el atributo color de la clase
        '''
        return self.__color__
