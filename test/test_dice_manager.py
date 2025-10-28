# tests/test_dice_manager.py
import unittest
from core.models.dice import Dice
from core.services.dice_manager import DiceManager
from unittest.mock import patch


class TestDiceManager(unittest.TestCase):
    
    @patch('random.randint', side_effect=[3,5])
    def test_tirar_dados_normales(self,mock_randint):
        """Test: Tirar dados con valores diferentes genera 2 movimientos"""
        dice1 = Dice()
        dice2 = Dice()
        manager = DiceManager(dice1, dice2)
        
        # Forzar valores diferentes
        manager.tirar_dados()
        
        disponibles = manager.obtener_dados_disponibles()
        self.assertEqual(len(disponibles), 2)
    
    @patch('random.randint', side_effect=[4,4])
    def test_tirar_dados_dobles(self,mock_randint):
        """Test: Tirar dobles genera 4 movimientos"""
        dice1 = Dice()
        dice2 = Dice()
        manager = DiceManager(dice1, dice2)
        
        # Forzar dobles
        manager.tirar_dados()
        
        disponibles = manager.obtener_dados_disponibles()
        self.assertEqual(len(disponibles), 4)
    
    def test_usar_dado(self):
        """Test: Usar un dado disponible lo remueve de la lista"""
        dice1 = Dice()
        dice2 = Dice()
        dice1.__numero__ = 3
        dice2.__numero__ = 5
        
        manager = DiceManager(dice1, dice2)
        manager.__dados_disponibles__ = [dice1, dice2]
        
        manager.usar_dado(3)
        
        self.assertEqual(len(manager.obtener_dados_disponibles()), 1)
    


if __name__ == '__main__':
    unittest.main()