import unittest
from core.backgammongame import BackgammonGame,PosNoDisponible,NoHayMovimientosPosibles, MovimientoInvalido
from core.board import Board
from core.checker import Checker
class TestCore(unittest.TestCase):

    def test_ocupar_casilla(self):
        juego = BackgammonGame()
        juego.__board__.__contenedor_fichas__ =  [
            [],[Checker("Blanco")],[],[],[],[], [],[],[],[],[],[],
            [],[],[],[],[],[], [],[],[],[],[],[]
        ]

        resultado_fichas = [
            [],[],[],[],[],[], [],[],[],[],[],[],
            [],[],[],[],[],[], [],[Checker("Blanco")],[],[],[],[]
        ]
        
        
        juego.ocupar_casilla(1,19)
        self.assertEqual(juego.__board__.__contenedor_fichas__[1],resultado_fichas[1])
        self.assertEqual(juego.__board__.__contenedor_fichas__[19][0].obtener_color(),resultado_fichas[19][0].obtener_color())
        self.assertEqual(len(juego.__board__.__contenedor_fichas__[19]),len(resultado_fichas[19]))
    def test_poner_ficha(self):
        juego = BackgammonGame()
        juego = BackgammonGame()
        juego.__board__.__contenedor_fichas__ =  [
            [],[],[],[],[],[], [],[],[],[],[],[],
            [],[],[],[],[],[], [],[],[],[],[],[]
        ]
        resultado_fichas = [
            [],[],[],[],[],[], [],[],[],[],[],[],
            [],[],[],[],[],[], [],[Checker("Blanco"),Checker("Blaco")],[],[],[],[]
        ]
        juego.__board__.poner_ficha(19,"Blanco")
        juego.__board__.poner_ficha(19,"Blanco") #se ponen dos fichas en la misma posición

        self.assertEqual(juego.__board__.__contenedor_fichas__[19][0].obtener_color(),resultado_fichas[19][0].obtener_color()) #comprueba que las fichas sean del mismo color
        self.assertEqual(len(juego.__board__.__contenedor_fichas__[19]),len(resultado_fichas[19]))#comprueba que la cantidad de fichas es correcta


    def test_quitar_ficha(self):
        juego = BackgammonGame()
        juego = BackgammonGame()
        juego.__board__.__contenedor_fichas__ =  [
            [],[],[],[],[],[], [],[],[],[],[],[],
            [],[],[],[],[],[], [],[Checker("Blanco"),Checker("Blaco")],[],[],[],[]
        ]
        resultado_fichas = [
            [],[],[],[],[],[], [],[],[],[],[],[],
            [],[],[],[],[],[], [],[],[],[],[],[]
        ]
        juego.__board__.quitar_ficha(19)
        juego.__board__.quitar_ficha(19)

        self.assertEqual(len(juego.__board__.__contenedor_fichas__[19]),len(resultado_fichas[19]))#comprueba que la cantidad de fichas es correcta


    def test_numero_en_rango_correcto(self):
        juego = BackgammonGame()
        for _ in range(100): 
            juego.__dice_1__.tirar_dado()
            numero = juego.__dice_1__.obtener_numero()
            self.assertGreaterEqual(numero, 1)
            self.assertLessEqual(numero, 6)
            self.assertIsInstance(numero, int)
    
    def test_todos_los_valores_posibles(self):
        juego = BackgammonGame()
        
        valores_obtenidos = set()
        for _ in range(1000):  
            juego.__dice_1__.tirar_dado()
            numero = juego.__dice_1__.obtener_numero()
            valores_obtenidos.add(numero)
        
       
        self.assertEqual(valores_obtenidos, {1, 2, 3, 4, 5, 6})
    
    def test_verificar_posicion_disp(self):
        juego = BackgammonGame()

        juego.__board__.__contenedor_fichas__ =  [
            [],[],[],[],[],[], [],[Checker("Blanco"),Checker("Blaco"),Checker("Blanco"),Checker("Blaco")],[],[],[],[],
            [],[Checker("Blanco")],[],[],[],[], [],[],[],[],[],[]
        ]
        
        self.assertTrue(juego.verificar_posicion_disponible(7))
        self.assertTrue(juego.verificar_posicion_disponible(13))
        self.assertTrue(juego.verificar_posicion_disponible(0))
    
    def test_verificar_no_posicion_disp(self):
        juego = BackgammonGame()

        juego.__board__.__contenedor_fichas__ =  [
            [],[],[],[],[],[], [],[Checker("Negro"),Checker("Negro"),Checker("Negro"),Checker("Negro")],[],[],[],[],
            [],[Checker("Negro"),Checker("Negro")],[],[],[],[], [],[],[],[],[],[]
        ]

        
        self.assertFalse(juego.verificar_posicion_disponible(7))
        self.assertFalse(juego.verificar_posicion_disponible(13))
    
    def test_verificar_movimientos_posibles(self):
    
        juego = BackgammonGame()
        juego.__dice_1__ = 3
        juego.__dice_2__ = 2
        
        juego.__board__.__contenedor_fichas__ =  [
            [],[],[],[],[],[], [],[Checker("Blanco")],[],[],[],[],
            [Checker("Blanco")],[],[],[],[],[], [],[],[],[],[],[]
        ]

        
        self.assertTrue(juego.verifificar_movimientos_posibles())

    def test_verificar_movimientos_posibles_no_hay(self):
    
        juego = BackgammonGame()
        juego.__dice_1__ = 3
        juego.__dice_2__ = 2
        
        juego.__board__.__contenedor_fichas__ =  [
            [],[],[],[],[],[], [],[Checker("Blanco")],[],[Checker("Negro"),Checker("Negro")],[Checker("Negro"),Checker("Negro")],[],
            [Checker("Negro"),Checker("Negro")],[],[],[],[],[], [],[],[],[],[],[]
        ]

        
        with self.assertRaises(NoHayMovimientosPosibles):
            juego.verifificar_movimientos_posibles()

    def test_sacar_ficha(self):
        juego = BackgammonGame()
        
        juego.__board__.__contenedor_fichas__ =  [
            [],[],[],[],[],[], [],[],[],[],[],[],
            [],[],[],[],[],[], [],[],[],[],[Checker("Blanco")],[Checker("Blanco")]
            ]
            
        self.assertTrue(juego.verificar_sacar_ficha(21,juego.__board__.__contenedor_fichas__))
        self.assertTrue(juego.verificar_sacar_ficha(24,juego.__board__.__contenedor_fichas__))
    
    def test_sacar_ficha_error(self):
        juego = BackgammonGame()
        juego.__board__.__contenedor_fichas__ =  [
            [],[],[],[],[],[], [],[],[],[],[],[],
            [],[],[],[Checker("Blanco")],[],[], [],[],[],[],[],[Checker("Blanco")]
            ]

        with self.assertRaises(MovimientoInvalido):    
            juego.verificar_sacar_ficha(24,juego.__board__.__contenedor_fichas__)
    
    def test_comer_ficha(self):
        juego = BackgammonGame()
        juego.__board__.__contenedor_fichas__ =  [
            [],[Checker("Blanco")],[],[],[],[], [],[],[],[],[],[],
            [],[],[],[],[],[], [],[Checker("Negro")],[],[],[],[]
        ]

        resultado_fichas = [
            [],[],[],[],[],[], [],[],[],[],[],[],
            [],[],[],[],[],[], [],[Checker("Blanco")],[],[],[],[]
        ]
        
        
        juego.ocupar_casilla(1,19)
        self.assertEqual(juego.__board__.__contenedor_fichas__[1],resultado_fichas[1])
        self.assertEqual(juego.__board__.__contenedor_fichas__[19][0].obtener_color(),resultado_fichas[19][0].obtener_color())
        self.assertEqual(len(juego.__board__.__contenedor_fichas__[19]),len(resultado_fichas[19]))
