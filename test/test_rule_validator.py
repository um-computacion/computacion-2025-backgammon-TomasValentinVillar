# tests/test_rule_validator.py
import unittest
from core.validators.rule_validator import RuleValidator
from core.board import Board
from core.models.dice import Dice
from core.models.checker import Checker


class TestRuleValidator(unittest.TestCase):
    
    # ═══════════════════════════════════════════════════════════════
    # Tests de puede_sacar_ficha() - BLANCAS
    # ═══════════════════════════════════════════════════════════════
    
    def test_puede_sacar_ficha_blanca_dado_exacto(self):
        """Test: Blancas pueden sacar con dado exacto"""
        validator = RuleValidator()
        board = Board()
        dice1 = Dice()
        dice2 = Dice()
        dados_disponibles = [dice1, dice2]
        
        board.poner_ficha(22, "Blanco")
        
        dice1.__numero__ = 2
        dice2.__numero__ = 3
        
        resultado = validator.puede_sacar_ficha(board, 22, "Blanco", dados_disponibles)
        
        self.assertEqual(resultado, 2)
    
    def test_puede_sacar_ficha_blanca_dado_mayor(self):
        """Test: Blancas pueden sacar con dado mayor si no hay fichas más atrás"""
        validator = RuleValidator()
        board = Board()
        dice1 = Dice()
        dice2 = Dice()
        dados_disponibles = [dice1, dice2]
        
        board.poner_ficha(23, "Blanco")
        
        dice1.__numero__ = 5
        dice2.__numero__ = 3
        
        resultado = validator.puede_sacar_ficha(board, 23, "Blanco", dados_disponibles)
        
        self.assertEqual(resultado, 3)
    
    def test_no_puede_sacar_blanca_fichas_fuera_home(self):
        """Test: Blancas NO pueden sacar si hay fichas fuera del home board"""
        validator = RuleValidator()
        board = Board()
        dice1 = Dice()
        dice2 = Dice()
        dados_disponibles = [dice1, dice2]
        
        board.poner_ficha(10, "Blanco")
        board.poner_ficha(22, "Blanco")
        
        dice1.__numero__ = 2
        dice2.__numero__ = 3
        
        with self.assertRaises(ValueError):
            validator.puede_sacar_ficha(board, 22, "Blanco", dados_disponibles)
    
    def test_no_puede_sacar_blanca_sin_dado_valido(self):
        """Test: Blancas NO pueden sacar si no hay dado válido"""
        validator = RuleValidator()
        board = Board()
        dice1 = Dice()
        dice2 = Dice()
        dados_disponibles = [dice1, dice2]
        
        board.poner_ficha(20, "Blanco")
        
        dice1.__numero__ = 2
        dice2.__numero__ = 3
        
        with self.assertRaises(ValueError):
            validator.puede_sacar_ficha(board, 20, "Blanco", dados_disponibles)
    
    # ═══════════════════════════════════════════════════════════════
    # Tests de puede_sacar_ficha() - NEGRAS
    # ═══════════════════════════════════════════════════════════════
    
    def test_puede_sacar_ficha_negra_dado_exacto(self):
        """Test: Negras pueden sacar con dado exacto"""
        validator = RuleValidator()
        board = Board()
        dice1 = Dice()
        dice2 = Dice()
        dados_disponibles = [dice1, dice2]
        
        board.poner_ficha(2, "Negro")
        
        dice1.__numero__ = 3
        dice2.__numero__ = 5
        
        resultado = validator.puede_sacar_ficha(board, 2, "Negro", dados_disponibles)
        
        self.assertEqual(resultado, 3)
    
    def test_puede_sacar_ficha_negra_dado_mayor(self):
        """Test: Negras pueden sacar con dado mayor si no hay fichas más atrás"""
        validator = RuleValidator()
        board = Board()
        dice1 = Dice()
        dice2 = Dice()
        dados_disponibles = [dice1, dice2]
        
        board.poner_ficha(0, "Negro")
        
        dice1.__numero__ = 6
        dice2.__numero__ = 4
        
        resultado = validator.puede_sacar_ficha(board, 0, "Negro", dados_disponibles)
        
        self.assertEqual(resultado, 4)
    
    def test_no_puede_sacar_negra_fichas_fuera_home(self):
        """Test: Negras NO pueden sacar si hay fichas fuera del home board"""
        validator = RuleValidator()
        board = Board()
        dice1 = Dice()
        dice2 = Dice()
        dados_disponibles = [dice1, dice2]
        
        board.poner_ficha(10, "Negro")
        board.poner_ficha(2, "Negro")
        
        dice1.__numero__ = 3
        dice2.__numero__ = 4
        
        with self.assertRaises(ValueError):
            validator.puede_sacar_ficha(board, 2, "Negro", dados_disponibles)
    
    # ═══════════════════════════════════════════════════════════════
    # Tests de tiene_fichas_comidas()
    # ═══════════════════════════════════════════════════════════════
    
    def test_tiene_fichas_comidas_true(self):
        """Test: Verificar si hay fichas comidas"""
        validator = RuleValidator()
        board = Board()
        
        board.__contenedor_fichas_blancas__.append(Checker("Blanco"))
        
        resultado = validator.tiene_fichas_comidas(board, "Blanco")
        
        self.assertTrue(resultado)
    
    def test_tiene_fichas_comidas_false(self):
        """Test: No hay fichas comidas"""
        validator = RuleValidator()
        board = Board()
        
        resultado = validator.tiene_fichas_comidas(board, "Blanco")
        
        self.assertFalse(resultado)
    
    # ═══════════════════════════════════════════════════════════════
    # Tests de todas_fichas_en_home_board()
    # ═══════════════════════════════════════════════════════════════
    
    def test_todas_fichas_en_home_board_blancas_true(self):
        """Test: Todas las fichas blancas están en home board"""
        validator = RuleValidator()
        board = Board()
        
        board.poner_ficha(18, "Blanco")
        board.poner_ficha(22, "Blanco")
        
        resultado = validator.todas_fichas_en_home_board(board, "Blanco")
        
        self.assertTrue(resultado)
    
    def test_todas_fichas_en_home_board_blancas_false(self):
        """Test: NO todas las fichas blancas están en home board"""
        validator = RuleValidator()
        board = Board()
        
        board.poner_ficha(10, "Blanco")
        board.poner_ficha(22, "Blanco")
        
        resultado = validator.todas_fichas_en_home_board(board, "Blanco")
        
        self.assertFalse(resultado)
    
    def test_todas_fichas_en_home_board_negras_true(self):
        """Test: Todas las fichas negras están en home board"""
        validator = RuleValidator()
        board = Board()
        
        board.poner_ficha(0, "Negro")
        board.poner_ficha(3, "Negro")
        
        resultado = validator.todas_fichas_en_home_board(board, "Negro")
        
        self.assertTrue(resultado)
    
    def test_todas_fichas_en_home_board_negras_false(self):
        """Test: NO todas las fichas negras están en home board"""
        validator = RuleValidator()
        board = Board()
        
        board.poner_ficha(10, "Negro")
        board.poner_ficha(2, "Negro")
        
        resultado = validator.todas_fichas_en_home_board(board, "Negro")
        
        self.assertFalse(resultado)


if __name__ == '__main__':
    unittest.main()