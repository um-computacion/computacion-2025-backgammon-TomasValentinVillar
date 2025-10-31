import unittest
from pygame_ui.board_adapter import BoardAdapter
from core.models.checker import Checker
from core.backgammongame import BackgammonGame

class TestBoardAdapter(unittest.TestCase):

    def test_board_adapter(self):
        juego = BackgammonGame()
        adapter = BoardAdapter(juego)
        juego.__board__.__contenedor_fichas__ = [
            [],[],[],[],[],[], [],[Checker("Negro"),Checker("Negro")],[Checker("Negro")],[Checker("Negro"),Checker("Negro"),Checker("Negro"),Checker("Negro"),Checker("Negro"),Checker("Negro")],[],[],
            [],[],[],[],[],[], [],[Checker("Blanco"),Checker("Blaco")],[Checker("Blanco")],[Checker("Blanco"),Checker("Blaco"),Checker("Blanco"),Checker("Blaco"),Checker("Blanco"),Checker("Blaco")],[],[]
        ]
        
        adapter.actualizar()
        board = adapter
        self.assertEqual(board.__pos__[19],("white",2))
        self.assertEqual(board.__pos__[20],("white",1))
        self.assertEqual(board.__pos__[21],("white",6))
        self.assertEqual(board.__pos__[7],("black",2))
        self.assertEqual(board.__pos__[8],("black",1))
        self.assertEqual(board.__pos__[9],("black",6))
        self.assertEqual(board.__pos__[0],None)


        

