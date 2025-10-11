# tests/test_rule_validator.py
import unittest
from core.validators.rule_validator import RuleValidator
from core.board import Board
from core.models.dice import Dice
from core.models.checker import Checker
from unittest.mock import patch

class TestRuleValidator(unittest.TestCase):
    
    def test_puede_sacar_ficha_blanca_en_home_board(self):
        """Test: Blancas pueden sacar ficha si todas están en home board (18-23)"""
        validator = RuleValidator()
        board = Board()
        dice1 = Dice()
        dice2 = Dice()
        
        # Colocar solo fichas blancas en home board
        board.poner_ficha(22, "Blanco")
        board.poner_ficha(20, "Blanco")
        
        # Dados que permiten sacar desde 22
        dice1.__numero__ = 2
        dice2.__numero__ = 3
        
        # Debe poder sacar desde posición 22 (distancia 2 al final)
        resultado = validator.puede_sacar_ficha(board, 22, "Blanco", dice1, dice2)
        self.assertTrue(resultado)
    
    def test_no_puede_sacar_si_hay_fichas_fuera_home_blancas(self):
        """Test: Blancas NO pueden sacar si hay fichas fuera del home board"""
        validator = RuleValidator()
        board = Board()
        dice1 = Dice()
        dice2 = Dice()
        
        # Colocar ficha blanca fuera del home board
        board.poner_ficha(10, "Blanco")
        board.poner_ficha(22, "Blanco")
        
        dice1.__numero__ = 2
        dice2.__numero__ = 3
        
        with self.assertRaises(ValueError):
            validator.puede_sacar_ficha(board, 22, "Blanco", dice1, dice2)
    
    def test_tiene_fichas_comidas(self):
        """Test: Verificar si hay fichas comidas"""
        validator = RuleValidator()
        board = Board()
        
        # Agregar ficha blanca comida
        board.__contenedor_fichas_blancas__.append(Checker("Blanco"))
        
        resultado = validator.tiene_fichas_comidas(board, "Blanco")
        self.assertTrue(resultado)
    
    def test_todas_fichas_en_home_board_blancas(self):
        """Test: Verificar que todas las fichas blancas están en home board"""
        validator = RuleValidator()
        board = Board()
        
        # Colocar fichas solo en home board (18-23)
        board.poner_ficha(18, "Blanco")
        board.poner_ficha(22, "Blanco")
        board.poner_ficha(20, "Blanco")
        
        resultado = validator.todas_fichas_en_home_board(board, "Blanco")
        self.assertTrue(resultado)
    
    def test_no_todas_fichas_en_home_board_blancas(self):
        """Test: Verificar que NO todas las fichas blancas están en home board"""
        validator = RuleValidator()
        board = Board()
        
        # Colocar ficha fuera del home board
        board.poner_ficha(10, "Blanco")
        board.poner_ficha(22, "Blanco")
        
        resultado = validator.todas_fichas_en_home_board(board, "Blanco")
        self.assertFalse(resultado)


if __name__ == '__main__':
    unittest.main()
