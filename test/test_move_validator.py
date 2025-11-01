# tests/test_move_validator.py
import unittest
from core.validators.move_validator import MoveValidator
from core.board import Board


class TestMoveValidator(unittest.TestCase):
    
    def test_posicion_vacia_es_disponible(self):
        """Test: Una posición vacía está disponible"""
        validator = MoveValidator()
        board = Board()
        board.inicializar_tablero()
        
        # Posición 1 está vacía
        resultado = validator.es_posicion_disponible(board, 1, "Blanco")
        self.assertTrue(resultado)
    
    def test_posicion_con_fichas_propias_es_disponible(self):
        """Test: Posición con fichas del mismo color está disponible"""
        validator = MoveValidator()
        board = Board()
        board.inicializar_tablero()
        
        # Posición 0 tiene 2 fichas blancas
        resultado = validator.es_posicion_disponible(board, 0, "Blanco")
        self.assertTrue(resultado)
    
    def test_posicion_bloqueada_no_es_disponible(self):
        """Test: Posición con 2+ fichas enemigas NO está disponible"""
        validator = MoveValidator()
        board = Board()
        board.inicializar_tablero()
        
        # Posición 5 tiene 5 fichas negras (bloqueada para blancas)
        resultado = validator.es_posicion_disponible(board, 5, "Blanco")
        self.assertFalse(resultado)
    
    def test_calcular_destino_blancas(self):
        """Test: Calcular destino para fichas blancas (van hacia arriba)"""
        validator = MoveValidator()
        
        resultado = validator.calcular_destino(0, 5, "Blanco")
        self.assertEqual(resultado, 5)
        
        resultado = validator.calcular_destino(10, 3, "Blanco")
        self.assertEqual(resultado, 13)
    
    def test_calcular_destino_negras(self):
        """Test: Calcular destino para fichas negras (van hacia abajo)"""
        validator = MoveValidator()
        
        resultado = validator.calcular_destino(23, 5, "Negro")
        self.assertEqual(resultado, 18)
        
        resultado = validator.calcular_destino(10, 3, "Negro")
        self.assertEqual(resultado, 7)


if __name__ == '__main__':
    unittest.main()