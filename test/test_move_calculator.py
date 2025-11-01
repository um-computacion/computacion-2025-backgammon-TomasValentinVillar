# tests/test_move_calculator.py
import unittest
from core.services.move_calculator import MoveCalculator
from core.validators.move_validator import MoveValidator
from core.validators.rule_validator import RuleValidator
from core.services.dice_manager import DiceManager
from core.board import Board
from core.models.dice import Dice
from core.models.checker import Checker
from unittest.mock import patch

class TestMoveCalculator(unittest.TestCase):
    
    @patch('random.randint', side_effect=[3, 5])
    def test_hay_movimientos_posibles_con_movimientos_normales(self,mock_randint):
        """Test: Hay movimientos posibles en tablero inicial"""
        move_validator = MoveValidator()
        rule_validator = RuleValidator()
        calculator = MoveCalculator(move_validator, rule_validator)
        board = Board()
        dice_manager = DiceManager()
        
        board.inicializar_tablero()
        dice_manager.tirar_dados()
        
        resultado = calculator.hay_movimientos_posibles(board, "Blanco", dice_manager)
        self.assertTrue(resultado)
    
    @patch('random.randint', side_effect=[3,2])
    def test_no_hay_movimientos_posibles(self,mock_randint):
        """Test: No hay movimientos cuando todo está bloqueado"""
        move_validator = MoveValidator()
        rule_validator = RuleValidator()
        calculator = MoveCalculator(move_validator, rule_validator)
        board = Board()
        dice_manager = DiceManager()
        
        # Blancas bloqueadas
        board.poner_ficha(0, "Blanco")
        
        # Bloquear todas las posiciones posibles
        for pos in range(1, 7):
            board.poner_ficha(pos, "Negro")
            board.poner_ficha(pos, "Negro")
        
        dice_manager.tirar_dados()
        
        with self.assertRaises(ValueError):
            calculator.hay_movimientos_posibles(board, "Blanco", dice_manager)
    
    def test_calcular_pasos_movimiento_blancas(self):
        """Test: Calcular pasos para fichas blancas"""
        move_validator = MoveValidator()
        rule_validator = RuleValidator()
        calculator = MoveCalculator(move_validator, rule_validator)
        
        pasos = calculator.calcular_pasos_movimiento(0, 5, "Blanco")
        self.assertEqual(pasos, 5)
        
        pasos = calculator.calcular_pasos_movimiento(10, 13, "Blanco")
        self.assertEqual(pasos, 3)
    
    def test_calcular_pasos_movimiento_negras(self):
        """Test: Calcular pasos para fichas negras"""
        move_validator = MoveValidator()
        rule_validator = RuleValidator()
        calculator = MoveCalculator(move_validator, rule_validator)
        
        pasos = calculator.calcular_pasos_movimiento(23, 18, "Negro")
        self.assertEqual(pasos, 5)
        
        pasos = calculator.calcular_pasos_movimiento(10, 7, "Negro")
        self.assertEqual(pasos, 3)
    
    @patch('random.randint', side_effect=[3,5])
    def test_hay_movimientos_desde_inicio(self,mock_randint):
        """Test: Hay movimientos cuando hay fichas comidas"""
        move_validator = MoveValidator()
        rule_validator = RuleValidator()
        calculator = MoveCalculator(move_validator, rule_validator)
        board = Board()
        dice_manager = DiceManager()
        
        # Agregar ficha blanca comida
        board.__contenedor_fichas_blancas__.append(Checker("Blanco"))
        
        # Posición 2 está vacía (puede entrar con dado 3)
        dice_manager.tirar_dados()
        
        resultado = calculator.hay_movimientos_posibles(board, "Blanco", dice_manager)
        self.assertTrue(resultado)


if __name__ == '__main__':
    unittest.main()