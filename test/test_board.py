import unittest
from core.backgammongame import BackgammonGame,NoHayMovimientosPosibles, MovimientoInvalido,Ganador
from core.board import Board
from core.models.checker import Checker
from core.models.dice import Dice
from unittest.mock import patch

class TestBoard(unittest.TestCase):
    def test_poner_ficha(self):
        board = Board()
        board.__contenedor_fichas__ =  [
            [],[],[],[],[],[], [],[],[],[],[],[],
            [],[],[],[],[],[], [],[],[],[],[],[]]

        resultado_fichas = [
            [],[],[],[],[],[], [],[],[],[],[],[],
            [],[],[],[],[],[], [],[Checker("Blanco"),Checker("Blaco")],[],[],[],[]
        ]
        board.poner_ficha(19,"Blanco")
        board.poner_ficha(19,"Blanco") #se ponen dos fichas en la misma posición

        self.assertEqual(board.__contenedor_fichas__[19][0].obtener_color(),resultado_fichas[19][0].obtener_color()) #comprueba que las fichas sean del mismo color
        self.assertEqual(len(board.__contenedor_fichas__[19]),len(resultado_fichas[19]))#comprueba que la cantidad de fichas es correcta


    def test_quitar_ficha(self):
        board = Board()
        board.__contenedor_fichas__ =  [
            [],[],[],[],[],[], [],[],[],[],[],[],
            [],[],[],[],[],[], [],[Checker("Blanco"),Checker("Blaco")],[],[],[],[]
        ]
        resultado_fichas = [
            [],[],[],[],[],[], [],[],[],[],[],[],
            [],[],[],[],[],[], [],[],[],[],[],[]
        ]
        board.quitar_ficha(19)
        board.quitar_ficha(19)

        self.assertEqual(len(board.__contenedor_fichas__[19]),len(resultado_fichas[19]))#comprueba que la cantidad de fichas es correcta

    def test_comer_ficha_negra(self):
        board = Board()
        turno = "Blanco"
        board.__contenedor_fichas__ = [
            [],[],[],[],[],[], [],[],[],[],[],[],
            [],[],[],[],[],[], [],[],[Checker("Negro")],[],[],[]
        ]
        board.comer_ficha(20, turno)

        self.assertEqual(len(board.__contenedor_fichas__[20]), 0)
        self.assertEqual(len(board.obtener_contenedor_negras()), 1)
        self.assertEqual(board.obtener_contenedor_negras()[0].obtener_color(), "Negro")
    
    def test_comer_ficha_blanca(self):
        board = Board()
        turno = "Negro"
        board.__contenedor_fichas__ = [
            [],[],[],[],[],[], [],[],[],[],[],[],
            [],[],[],[],[],[], [],[],[Checker("Blanco")],[],[],[]
        ]
        board.comer_ficha(20, turno)

        self.assertEqual(len(board.__contenedor_fichas__[20]), 0)
        self.assertEqual(len(board.obtener_contenedor_blancas()), 1)
        self.assertEqual(board.obtener_contenedor_blancas()[0].obtener_color(), "Blanco")
    
    def test_sacar_ficha_blanca(self):
        board = Board()
        turno = "Blanco"
        board.__contenedor_fichas__ = [
            [],[],[],[],[],[], [],[],[],[],[],[],
            [],[],[],[],[],[], [],[],[Checker("Blanco")],[],[],[]
        ]
        board.sacar_ficha(20, turno)

        self.assertEqual(len(board.__contenedor_fichas__[20]), 0)
        self.assertEqual(len(board.obtener_contenedor_blancas_sacadas()), 1)
        self.assertEqual(board.obtener_contenedor_blancas_sacadas()[0].obtener_color(), "Blanco")
    
    def test_sacar_ficha_negra(self):
        board = Board()
        turno = "Negro"
        board.__contenedor_fichas__ = [
            [],[],[],[],[],[], [],[],[],[],[],[],
            [],[],[],[],[],[], [],[],[Checker("Negro")],[],[],[]
        ]
        board.sacar_ficha(20, turno)

        self.assertEqual(len(board.__contenedor_fichas__[20]), 0)
        self.assertEqual(len(board.obtener_contenedor_negras_sacadas()), 1)
        self.assertEqual(board.obtener_contenedor_negras_sacadas()[0].obtener_color(), "Negro")

    def test_verficar_fichas_sacadas_15_blanco(self):
        board = Board()
        turno = "Blanco"
        board.__contenedor_fichas_blancas_sacadas__ = [
            Checker("Blanco"), Checker("Blanco"), Checker("Blanco"),
            Checker("Blanco"), Checker("Blanco"), Checker("Blanco"),
            Checker("Blanco"), Checker("Blanco"), Checker("Blanco"),
            Checker("Blanco"), Checker("Blanco"), Checker("Blanco"),
            Checker("Blanco"), Checker("Blanco"), Checker("Blanco"),
        ]
        self.assertTrue(board.verficar_fichas_sacadas_15(turno))

    def test_verficar_fichas_sacadas_15_negro(self):
        board = Board()
        turno = "Negro"
        board.__contenedor_fichas_negras_sacadas__ = [
            Checker("Negro"), Checker("Negro"), Checker("Negro"),
            Checker("Negro"), Checker("Negro"), Checker("Negro"),
            Checker("Negro"), Checker("Negro"), Checker("Negro"),
            Checker("Negro"), Checker("Negro"), Checker("Negro"),
            Checker("Negro"), Checker("Negro"), Checker("Negro"),
        ]
        self.assertTrue(board.verficar_fichas_sacadas_15(turno))  
    
    def test_quitar_ficha_comida(self):
        board = Board()
        turno = "Blanco"
        board.__contenedor_fichas_blancas__ = [Checker("Blanco")]
        board.quitar_ficha_comida(turno)
        self.assertEqual(len(board.obtener_contenedor_blancas()),0)
    
    def test_quitar_ficha_comida_turno_negro(self):
        board = Board()
        turno = "Negro"
        board.__contenedor_fichas_negras__ = [Checker("Negras")]
        board.quitar_ficha_comida(turno)
        self.assertEqual(len(board.obtener_contenedor_negras()),0)

    def test__get_symbol_W(self):
        board = Board()
        self.assertEqual(board._get_piece_symbol(Checker("Blanco")),"W")
    
    def test__get_symbol_B(self):
        board = Board()
        self.assertEqual(board._get_piece_symbol(Checker("Negro")),"B")
    
    def test_draw_full_board(self):
        board = Board()
        board.__contenedor_fichas__ =  [
            [Checker("Blanco"),Checker("Blanco"),Checker("Blanco")],[Checker("Blanco"),Checker("Blanco"),Checker("Blanco"),Checker("Blanco"),Checker("Blanco"),Checker("Blanco"),Checker("Blanco"),Checker("Blanco")],[],[],[],[], [],[],[],[],[],[],
            [],[],[],[],[],[], [],[],[],[],[Checker("Negro"),Checker("Negro"),Checker("Negro")],[Checker("Negro")]
        ]
        board_draw = board.draw_full_board()
        self.assertEqual(
            board_draw,
            [ # 10
                [ # 1
                    ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'W', 'W', 
                ],
                [ # 2
                    ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'W', 'W', 
                ],
                [ # 3
                    ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'W', 'W', 
                ],
                [ # 4
                    ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'W', ' ', 
                ],
                [ # 5
                    ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '4', ' ', 
                ],
                [ # 6
                    ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'B', 'B', 
                ],
                [ # 7
                    ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'B', ' ', 
                ],
                [ # 8
                    ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'B', ' ', 
                ],
                [ # 9
                    ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 
                ],
                [ # 10
                    ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 
                ]
            ]
        )
    
    def test_inicilazar_tablero(self):
        board = Board()
        board.inicializar_tablero()
        self.assertEqual(len(board.obtener_contenedor_fichas()[0]),2)
        self.assertEqual(len(board.obtener_contenedor_fichas()[11]),5)
        self.assertEqual(len(board.obtener_contenedor_fichas()[16]),3)
        self.assertEqual(len(board.obtener_contenedor_fichas()[18]),5)
        self.assertEqual(len(board.obtener_contenedor_fichas()[23]),2)
        self.assertEqual(len(board.obtener_contenedor_fichas()[12]),5)
        self.assertEqual(len(board.obtener_contenedor_fichas()[7]),3)
        self.assertEqual(len(board.obtener_contenedor_fichas()[5]),5)
        self.assertEqual(board.obtener_contenedor_fichas()[0][0].obtener_color(),"Blanco")
        self.assertEqual(board.obtener_contenedor_fichas()[11][0].obtener_color(),"Blanco")
        self.assertEqual(board.obtener_contenedor_fichas()[16][0].obtener_color(),"Blanco")
        self.assertEqual(board.obtener_contenedor_fichas()[18][0].obtener_color(),"Blanco")
        self.assertEqual(board.obtener_contenedor_fichas()[23][0].obtener_color(),"Negro")
        self.assertEqual(board.obtener_contenedor_fichas()[12][0].obtener_color(),"Negro")
        self.assertEqual(board.obtener_contenedor_fichas()[7][0].obtener_color(),"Negro")
        self.assertEqual(board.obtener_contenedor_fichas()[5][0].obtener_color(),"Negro")
    
    def test_verificar_ficha_comida(self):
        board = Board()
        turno = "Blanco"
        board.__contenedor_fichas_blancas__.append(Checker("Blanco"))
        self.assertTrue(board.verificar_ficha_comida(turno))
    
    def test_verificar_ficha_comida_no_hay(self):
        board = Board()
        turno = "Blanco"
        self.assertFalse(board.verificar_ficha_comida(turno))
    
    def test_verificar_ficha_comida_negra(self):
        board = Board()
        turno = "Negro"
        board.__contenedor_fichas_negras__.append(Checker("Negro"))
        self.assertTrue(board.verificar_ficha_comida(turno))
    
    def test_verificar_ficha_comida_negra_no_hay(self):
        board = Board()
        turno = "Negro"
        self.assertFalse(board.verificar_ficha_comida(turno))
    
    def test_obtener_cantidad_de_fichas_comidas(self):
        board = Board()
        board.__contenedor_fichas_blancas__.extend([Checker('Blanco'),Checker('Blanco')])
        
        self.assertEqual(board.obtener_cantidad_de_fichas_comidas("Blanco"), 2)
    
    def test_obtener_cantidad_de_fichas_comidas_negro(self):
        board = Board()
        board.__contenedor_fichas_negras__.extend([Checker('Negro'),Checker('Negro')])
        
        self.assertEqual(board.obtener_cantidad_de_fichas_comidas("Negro"), 2)
