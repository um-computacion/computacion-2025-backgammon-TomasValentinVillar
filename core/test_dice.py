import unittest
from core.backgammongame import BackgammonGame,NoHayMovimientosPosibles, MovimientoInvalido,Ganador
from core.board import Board
from core.models.checker import Checker
from core.models.dice import Dice
from unittest.mock import patch

class TestDice(unittest.TestCase):
    def test_numero_en_rango_correcto(self):
        dado = Dice()
        for _ in range(100): 
            dado.tirar_dado()
            numero = dado.obtener_numero()
            self.assertGreaterEqual(numero, 1)
            self.assertLessEqual(numero, 6)
            self.assertIsInstance(numero, int)
    
    def test_todos_los_valores_posibles(self):
        dado = Dice()
        
        valores_obtenidos = set()
        for _ in range(1000):  
            dado.tirar_dado()
            numero = dado.obtener_numero()
            valores_obtenidos.add(numero)
       
        self.assertEqual(valores_obtenidos, {1, 2, 3, 4, 5, 6})
    
    @patch('random.randint', side_effect=[3])
    def test_tirar_dado(self, mock_randint):
        dice = Dice()
        dice.tirar_dado()
        
        self.assertEqual(mock_randint.call_count,1)
        mock_randint.assert_any_call(1, 6)
        self.assertEqual(dice.obtener_numero(), 3)