class Player:
    def __init__(self,nombre,ficha,estado):
        self.__nombre__ = nombre
        self.__ficha__ = ficha
        self.__estado__ = estado
    
    def obtener_nombre(self):
        return self.__nombre__
    
    def obtener_ficha(self):
        return self.__ficha__
    
    def obtener_estado(self):
        return self.__estado__