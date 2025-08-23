import unittest
from core.backgammongame import BackgammonGame
from core.board import Board

class TestCore(unittest.TestCase):

    def test_ocupar_casilla(self):
        juego = BackgammonGame()
        juego.__board__.__contenedor_fichas__ =  [
            [0,0,0,0,0,0],[0,0,0,0,0,0],
            [0,0,0,1,0,0],[0,0,0,0,0,0]]
        juego.__board__.__contenedor_color__ = [
            ["","","","","",""],["","","","","",""],
            ["","","","B","",""],["","","","","",""]
        ]
        resultado_fichas = [
            [0,0,0,0,0,0],[0,0,0,0,0,0],
            [0,0,0,0,0,0],[0,1,0,0,0,0]]
        
        resultado_color = [
            ["","","","","",""],["","","","","",""],
            ["","","","","",""],["","B","","","",""]
        ]
        juego.ocupar_casilla(2,3,3,1)
        self.assertEqual(juego.__board__.__contenedor_fichas__,resultado_fichas)
        self.assertEqual(juego.__board__.__contenedor_color__,resultado_color)
    def test_poner_ficha(self):
        juego = BackgammonGame()
        juego.__board__.__contenedor_fichas__ =  [
            [0,0,0,0,0,0],[0,0,0,0,0,0],
            [0,0,0,0,0,0],[0,0,0,0,0,0]]
        juego.__board__.__contenedor_color__ = [
            ["","","","","",""],["","","","","",""],
            ["","","","","",""],["","","","","",""]
        ]
        resultado_fichas = [
            [0,0,0,0,0,0],[0,0,0,0,0,0],
            [0,0,0,0,0,0],[0,2,0,0,0,0]]
        
        resultado_color = [
            ["","","","","",""],["","","","","",""],
            ["","","","","",""],["","B","","","",""]
        ]
        juego.__board__.poner_ficha(3,1,"B")
        juego.__board__.poner_ficha(3,1,"B") #se ponen dos fichas en la misma posición
        self.assertEqual(juego.__board__.__contenedor_fichas__,resultado_fichas)
        self.assertEqual(juego.__board__.__contenedor_color__,resultado_color)
    def test_quitar_ficha(self):
        juego = BackgammonGame()
        juego.__board__.__contenedor_fichas__ =  [
            [0,0,0,0,0,0],[0,0,0,0,0,0],
            [0,1,0,0,0,0],[0,0,0,0,0,0]]
        juego.__board__.__contenedor_color__ = [
            ["","","","","",""],["","","","","",""],
            ["","B","","","",""],["","","","","",""]
        ]
        resultado_fichas = [
            [0,0,0,0,0,0],[0,0,0,0,0,0],
            [0,0,0,0,0,0],[0,0,0,0,0,0]]
        
        resultado_color = [
            ["","","","","",""],["","","","","",""],
            ["","","","","",""],["","","","","",""]
        ]
        juego.__board__.quitar_ficha(2,1,"B")
        self.assertEqual(juego.__board__.__contenedor_fichas__,resultado_fichas)
        self.assertEqual(juego.__board__.__contenedor_color__,resultado_color)

    def test_numero_en_rango_correcto(self):
        juego = BackgammonGame()
        for _ in range(100): 
            numero = juego.__dice_1__.tirar_dado()
            self.assertGreaterEqual(numero, 1)
            self.assertLessEqual(numero, 6)
            self.assertIsInstance(numero, int)
    
    def test_todos_los_valores_posibles(self):
        juego = BackgammonGame()
        
        valores_obtenidos = set()
        for _ in range(1000):  
            numero = juego.__dice_1__.tirar_dado()
            valores_obtenidos.add(numero)
        
       
        self.assertEqual(valores_obtenidos, {1, 2, 3, 4, 5, 6})