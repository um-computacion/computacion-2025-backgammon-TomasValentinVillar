# tests/test_dice_manager.py
import unittest
from core.models.dice import Dice
from core.services.dice_manager import DiceManager
from unittest.mock import patch


class TestDiceManager(unittest.TestCase):
    
    @patch('random.randint', side_effect=[3,5])
    def test_tirar_dados_normales(self,mock_randint):
        """Test: Tirar dados con valores diferentes genera 2 movimientos"""
        manager = DiceManager()
        
        # Forzar valores diferentes
        manager.tirar_dados()
        
        disponibles = manager.obtener_dados_disponibles()
        self.assertEqual(len(disponibles), 2)
    
    @patch('random.randint', side_effect=[4,4])
    def test_tirar_dados_dobles(self,mock_randint):
        """Test: Tirar dobles genera 4 movimientos"""
        manager = DiceManager()
        
        # Forzar dobles
        manager.tirar_dados()
        
        disponibles = manager.obtener_dados_disponibles()
        self.assertEqual(len(disponibles), 4)
    
    @patch('random.randint', side_effect=[3, 5])
    def test_usar_dado(self,mock_randint):
        """Test: Usar un dado disponible lo remueve de la lista"""
        manager = DiceManager()
        manager.tirar_dados()
        manager.usar_dado(3)
        
        self.assertEqual(len(manager.obtener_dados_disponibles()), 1)
    


if __name__ == '__main__':
    unittest.main()