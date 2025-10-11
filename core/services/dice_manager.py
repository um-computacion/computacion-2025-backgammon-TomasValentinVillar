# core/services/dice_manager.py

class DiceManager:
    """
    Responsabilidad: Gestionar los dados y movimientos disponibles
    Cumple con SRP: Solo maneja la lógica de dados
    """
    
    def __init__(self, dice1, dice2):
        """
        Args:
            dice1, dice2: Instancias de Dice
        """
        self.__dice1__ = dice1
        self.__dice2__ = dice2
        self.__dados_disponibles__ = []
    
    def tirar_dados(self):
        """
        Tira ambos dados y actualiza la lista de dados disponibles
        Si son dobles, se pueden hacer 4 movimientos
        """
        self.__dice1__.tirar_dado()
        self.__dice2__.tirar_dado()
        
        if self.__dice1__.obtener_numero() == self.__dice2__.obtener_numero():
            # Dobles: 4 movimientos
            self.__dados_disponibles__ = [self.__dice1__, self.__dice1__, self.__dice1__, self.__dice1__]
        else:
            # Normal: 2 movimientos
            self.__dados_disponibles__ = [self.__dice1__, self.__dice2__]
    
    def usar_dado(self, pasos):
        """
        Marca un dado como usado según los pasos del movimiento
        
        Args:
            pasos: int - número de pasos del movimiento
            
        Returns:
            bool - True si se pudo usar el dado
            
        Raises:
            ValueError si no hay dado disponible para esos pasos
        """
        # Intentar usar dado 1
        if self.__dice1__.obtener_numero() == pasos and self.__dice1__ in self.__dados_disponibles__:
            self.__dados_disponibles__.remove(self.__dice1__)
            return True
        
        # Intentar usar dado 2
        if self.__dice2__.obtener_numero() == pasos and self.__dice2__ in self.__dados_disponibles__:
            self.__dados_disponibles__.remove(self.__dice2__)
            return True
        
        raise ValueError(f"No hay dado disponible para {pasos} pasos")
    
    def usar_dados_combinados(self, pasos):
        """
        Usa ambos dados para un movimiento combinado
        
        Args:
            pasos: int - total de pasos (suma de ambos dados)
            
        Returns:
            bool - True si se pudieron usar ambos dados
            
        Raises:
            ValueError si no se pueden combinar los dados
        """
        total = self.__dice1__.obtener_numero() + self.__dice2__.obtener_numero()
        
        if pasos != total:
            raise ValueError(f"El movimiento no coincide con la suma de dados ({total})")
        
        # Remover ambos dados
        if len(self.__dados_disponibles__) >= 2:
            self.__dados_disponibles__.remove(self.__dice1__)
            
            if self.__dice1__.obtener_numero() == self.__dice2__.obtener_numero():
                # Si son dobles, remover dos del mismo
                self.__dados_disponibles__.remove(self.__dice1__)
            else:
                # Si son diferentes, remover el otro
                self.__dados_disponibles__.remove(self.__dice2__)
            
            return True
        
        raise ValueError("No hay suficientes dados disponibles")
    
    def tiene_dados_disponibles(self):
        """
        Verifica si quedan dados por usar
        
        Returns:
            bool - True si quedan dados
        """
        return len(self.__dados_disponibles__) > 0
    
    def obtener_dados_disponibles(self):
        """
        Retorna la lista de dados disponibles
        
        Returns:
            list - lista de instancias de Dice disponibles
        """
        return self.__dados_disponibles__.copy()
    
    def obtener_valores(self):
        """
        Retorna los valores de los dados
        
        Returns:
            tuple - (valor_dado1, valor_dado2)
        """
        return (self.__dice1__.obtener_numero(), self.__dice2__.obtener_numero())