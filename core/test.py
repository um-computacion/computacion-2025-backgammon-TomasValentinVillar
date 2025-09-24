import unittest
from core.backgammongame import BackgammonGame,PosNoDisponible,NoHayMovimientosPosibles, MovimientoInvalido
from core.board import Board
from core.checker import Checker
from core.dice import Dice
from unittest.mock import patch
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
    def test_ocupar_casilla_come_ficha(self):
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
        self.assertEqual(len(juego.__board__.obtener_contenedor_negras()),1)
        self.assertEqual(juego.__board__.obtener_contenedor_negras()[0].obtener_color(),"Negro")

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
        juego.__dice_1__.__numero__ = 3
        juego.__dice_2__.__numero__ = 2
        
        juego.__board__.__contenedor_fichas__ =  [
            [],[],[],[],[],[], [],[Checker("Blanco")],[],[],[],[],
            [Checker("Blanco")],[],[],[],[],[], [],[],[],[],[],[]
        ]

        
        self.assertTrue(juego.verifificar_movimientos_posibles())

    def test_verificar_movimientos_posibles_no_hay(self):
    
        juego = BackgammonGame()
        juego.__dice_1__.__numero__ = 3
        juego.__dice_2__.__numero__ = 2
        
        juego.__board__.__contenedor_fichas__ =  [
            [],[],[],[],[],[], [],[Checker("Blanco")],[],[Checker("Negro"),Checker("Negro")],[Checker("Negro"),Checker("Negro")],[],
            [Checker("Negro"),Checker("Negro")],[],[],[],[],[], [],[],[],[],[],[]
        ]
        with self.assertRaises(NoHayMovimientosPosibles):
            juego.verifificar_movimientos_posibles()
    def test_verificar_movimientos_posibles_negro(self):
    
        juego = BackgammonGame()

        juego.__turno__ = "Negro"
        juego.__dice_1__.__numero__ = 3
        juego.__dice_2__.__numero__ = 2
        
        juego.__board__.__contenedor_fichas__ =  [
            [],[],[],[],[],[], [],[Checker("Negro")],[],[],[],[],
            [Checker("Negro")],[],[],[],[],[], [],[],[],[],[],[]
        ]        
        self.assertTrue(juego.verifificar_movimientos_posibles())
    
    def test_verificar_movimientos_posibles_no_hay_negro(self):
    
        juego = BackgammonGame()
        juego.__turno__ = "Negro"
        juego.__dice_1__.__numero__ = 3
        juego.__dice_2__.__numero__ = 2
        
        juego.__board__.__contenedor_fichas__ =  [
            [],[],[],[],[],[], [],[Checker("Blanco"),Checker("Blanco")],[],[Checker("Blanco"),Checker("Blanco")],[Checker("Blanco"),Checker("Blanco")],[],
            [Checker("Negro")],[],[],[],[],[], [],[],[],[],[],[]
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
    
    def test_sacar_ficha_negro(self):
        juego = BackgammonGame()
        juego.__turno__ = "Negro"
        juego.__board__.__contenedor_fichas__ =  [
            [Checker("Negro")],[Checker("Negro")],[],[],[],[], [],[],[],[],[],[],
            [],[],[],[],[],[], [],[],[],[],[],[]
            ]
            
        self.assertTrue(juego.verificar_sacar_ficha(6,juego.__board__.__contenedor_fichas__))
        self.assertTrue(juego.verificar_sacar_ficha(-1,juego.__board__.__contenedor_fichas__)) #quitar ficha de tablero
    
    def test_sacar_ficha_error_negro(self):
        juego = BackgammonGame()
        juego.__turno__ = "Negro"

        juego.__board__.__contenedor_fichas__ =  [
            [Checker("Negro")],[],[],[],[],[], [],[],[],[],[],[],
            [],[],[],[Checker("Negro")],[],[], [],[],[],[],[],[]
            ]

        with self.assertRaises(MovimientoInvalido):    
            juego.verificar_sacar_ficha(-1,juego.__board__.__contenedor_fichas__)# se intenta quitar ficha de tablero
    

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

        
    @patch('random.randint', side_effect=[3, 5])
    def test_tirar_dados_diferentes(self, mock_randint):
        game = BackgammonGame()
        game.tirar_dados()
        
        # Verificamos que se llamó randint dos veces
        self.assertEqual(mock_randint.call_count, 2)
        mock_randint.assert_any_call(1, 6)
        
        # Verificamos los valores de los dados
        self.assertEqual(game.__dice_1__.obtener_numero(), 3)
        self.assertEqual(game.__dice_2__.obtener_numero(), 5)
    
    @patch('random.randint', return_value=4)
    def test_tirar_dados_iguales(self, mock_randint):
        game = BackgammonGame()
        game.tirar_dados()
        
        # Ambos dados deberían tener el mismo valor
        self.assertEqual(game.__dice_1__.obtener_numero(), 4)
        self.assertEqual(game.__dice_2__.obtener_numero(), 4)
        self.assertEqual(mock_randint.call_count, 2)
    
    @patch('random.randint', side_effect=[3, 5])
    def test_cantidad_mov(self, mock_randint):
        juego = BackgammonGame()
        juego.tirar_dados()

        self.assertEqual(len(juego.__dados_disponibles__),2)
        self.assertEqual((juego.__dados_disponibles__[0].obtener_numero()), 3)
        self.assertEqual((juego.__dados_disponibles__[1].obtener_numero()), 5)

    @patch('random.randint', return_value = 1)
    def test_cantidad_mov_iguales(self, randit_patched):
        juego = BackgammonGame()
        juego.tirar_dados()


        self.assertEqual(len(juego.__dados_disponibles__),4)
        self.assertEqual((juego.__dados_disponibles__[0].obtener_numero()),1)
        self.assertEqual((juego.__dados_disponibles__[1].obtener_numero()), 1)
        self.assertEqual((juego.__dados_disponibles__[2].obtener_numero()), 1)
        self.assertEqual((juego.__dados_disponibles__[3].obtener_numero()), 1)

    @patch('random.randint', side_effect=[2, 5])
    def test_verificar_movimientos_y_dados_blanco(self,mock_randint):
        juego = BackgammonGame()
        juego.tirar_dados()

        self.assertTrue(juego.verificar_movimientos_y_dados(10,15))
        self.assertEqual(len(juego.__dados_disponibles__), 1)
        self.assertEqual(juego.__dados_disponibles__[0].obtener_numero(), 2)
    
    @patch('random.randint', side_effect=[5, 5])
    def test_verificar_movimientos_y_dados_blanco_doble(self,mock_randint):
        juego = BackgammonGame()
        juego.tirar_dados()


        self.assertTrue(juego.verificar_movimientos_y_dados(10,20))
        self.assertEqual(len(juego.__dados_disponibles__), 2)
        self.assertEqual(juego.__dados_disponibles__[0].obtener_numero(), 5)
        self.assertEqual(juego.__dados_disponibles__[0].obtener_numero(), 5)
    
    @patch('random.randint', side_effect=[2, 5])
    def test_verificar_movimientos_y_dados_negro(self,mock_randint):
        juego = BackgammonGame()
        juego.__turno__ = "Negro"
        juego.tirar_dados()

        self.assertTrue(juego.verificar_movimientos_y_dados(15, 10))
        self.assertEqual(len(juego.__dados_disponibles__), 1)
        self.assertEqual(juego.__dados_disponibles__[0].obtener_numero(), 2)
    
    @patch('random.randint', side_effect=[5, 5])
    def test_verificar_movimientos_y_dados_negro_doble(self,mock_randint):
        juego = BackgammonGame()
        juego.__turno__ = "Negro"
        juego.tirar_dados()


        self.assertTrue(juego.verificar_movimientos_y_dados(20,10))
        self.assertEqual(len(juego.__dados_disponibles__), 2)
        self.assertEqual(juego.__dados_disponibles__[0].obtener_numero(), 5)
        self.assertEqual(juego.__dados_disponibles__[0].obtener_numero(), 5)

    @patch('random.randint', side_effect=[5, 2])
    def test_verificar_movimientos_y_dados_error(self,mock_randint):
        juego = BackgammonGame()
        juego.tirar_dados()

        with self.assertRaises(MovimientoInvalido):
            juego.verificar_movimientos_y_dados(5,9)
        with self.assertRaises(MovimientoInvalido):
            juego.__turno__ = "Negro"
            juego.verificar_movimientos_y_dados(15,11)
    
    def test_comer_ficha_negra(self):
        juego = BackgammonGame()
        juego.__board__.__contenedor_fichas__ = [
            [],[],[],[],[],[], [],[],[],[],[],[],
            [],[],[],[],[],[], [],[],[Checker("Negro")],[],[],[]
        ]
        juego.__board__.comer_ficha(20, juego.__turno__)

        self.assertEqual(len(juego.__board__.__contenedor_fichas__[20]), 0)
        self.assertEqual(len(juego.__board__.obtener_contenedor_negras()), 1)
        self.assertEqual(juego.__board__.obtener_contenedor_negras()[0].obtener_color(), "Negro")
    
    def test_comer_ficha_blanca(self):
        juego = BackgammonGame()
        juego.__turno__ = "Negro"
        juego.__board__.__contenedor_fichas__ = [
            [],[],[],[],[],[], [],[],[],[],[],[],
            [],[],[],[],[],[], [],[],[Checker("Blanco")],[],[],[]
        ]
        juego.__board__.comer_ficha(20, juego.__turno__)

        self.assertEqual(len(juego.__board__.__contenedor_fichas__[20]), 0)
        self.assertEqual(len(juego.__board__.obtener_contenedor_blancas()), 1)
        self.assertEqual(juego.__board__.obtener_contenedor_blancas()[0].obtener_color(), "Blanco")
    
    def test_sacar_ficha_blanca(self):
        juego = BackgammonGame()
        juego.__board__.__contenedor_fichas__ = [
            [],[],[],[],[],[], [],[],[],[],[],[],
            [],[],[],[],[],[], [],[],[Checker("Blanco")],[],[],[]
        ]
        juego.__board__.sacar_ficha(20, juego.__turno__)

        self.assertEqual(len(juego.__board__.__contenedor_fichas__[20]), 0)
        self.assertEqual(len(juego.__board__.obtener_contenedor_blancas_sacadas()), 1)
        self.assertEqual(juego.__board__.obtener_contenedor_blancas_sacadas()[0].obtener_color(), "Blanco")
    
    def test_sacar_ficha_negra(self):
        juego = BackgammonGame()
        juego.__turno__ = "Negro"
        juego.__board__.__contenedor_fichas__ = [
            [],[],[],[],[],[], [],[],[],[],[],[],
            [],[],[],[],[],[], [],[],[Checker("Negro")],[],[],[]
        ]
        juego.__board__.sacar_ficha(20, juego.__turno__)

        self.assertEqual(len(juego.__board__.__contenedor_fichas__[20]), 0)
        self.assertEqual(len(juego.__board__.obtener_contenedor_negras_sacadas()), 1)
        self.assertEqual(juego.__board__.obtener_contenedor_negras_sacadas()[0].obtener_color(), "Negro")
    
    def test_varificar_cambio_turno_cambia(self):
        juego = BackgammonGame()
        juego.__dados_disponibles__ = [] #lista sin dados disponibles

        juego.verificar_cambio_turno()
        self.assertEqual(juego.__turno__, "Negro")

    @patch('random.randint', side_effect=[5, 2])
    def test_varificar_cambio_turno_no_cambia(self, mock_randint):
        juego = BackgammonGame()
        juego.tirar_dados()

        self.assertTrue(juego.verificar_cambio_turno())

    def test_crear_jugador(self):
        juego = BackgammonGame()
        juego.crear_jugador('Tomas', 'Blanco', 'Jugando')
        self.assertEqual('Tomas', juego.obtener_players()['Blanco'].obtener_nombre())
        self.assertEqual('Blanco', juego.obtener_players()['Blanco'].obtener_ficha())
    
    def test_verficar_fichas_sacadas_15_blanco(self):
        juego = BackgammonGame()
        juego.__board__.__contenedor_fichas_blancas_sacadas__ = [
            Checker("Blanco"), Checker("Blanco"), Checker("Blanco"),
            Checker("Blanco"), Checker("Blanco"), Checker("Blanco"),
            Checker("Blanco"), Checker("Blanco"), Checker("Blanco"),
            Checker("Blanco"), Checker("Blanco"), Checker("Blanco"),
            Checker("Blanco"), Checker("Blanco"), Checker("Blanco"),
        ]
        self.assertTrue(juego.__board__.verficar_fichas_sacadas_15(juego.__turno__))

    def test_verficar_fichas_sacadas_15_negro(self):
        juego = BackgammonGame()
        juego.__turno__ = "Negro"
        juego.__board__.__contenedor_fichas_negras_sacadas__ = [
            Checker("Negro"), Checker("Negro"), Checker("Negro"),
            Checker("Negro"), Checker("Negro"), Checker("Negro"),
            Checker("Negro"), Checker("Negro"), Checker("Negro"),
            Checker("Negro"), Checker("Negro"), Checker("Negro"),
            Checker("Negro"), Checker("Negro"), Checker("Negro"),
        ]
        self.assertTrue(juego.__board__.verficar_fichas_sacadas_15(juego.__turno__))
    
    def test_cambio_de_turno_blanco(self):
        juego = BackgammonGame()
        juego.cambiar_turno()
        self.assertEqual(juego.__turno__,"Negro")
    
    def test_cambio_de_turno_negro(self):
        juego = BackgammonGame()
        juego.__turno__ = "Negro"
        juego.cambiar_turno()
        self.assertEqual(juego.__turno__,"Blanco")

    @patch('random.randint', side_effect=[3, 2])
    def test_realizar_moviemto(self,mock_randint):
        juego = BackgammonGame()
        juego.tirar_dados()
        juego.__board__.__contenedor_fichas__ =  [
            [Checker("Blanco"),Checker("Blanco")],[],[],[],[],[Checker("Negro"),Checker("Negro"),Checker("Negro"),Checker("Negro"),Checker("Negro")], [],[Checker("Negro"),Checker("Negro"),Checker("Negro")],[],[],[],[Checker("Blanco"),Checker("Blanco"),Checker("Blanco"),Checker("Blanco"),Checker("Blanco")],
            [Checker("Negro"),Checker("Negro"),Checker("Negro"),Checker("Negro"),Checker("Negro")],[],[],[],[Checker("Blanco"),Checker("Blanco"),Checker("Blanco")],[], [Checker("Blanco"),Checker("Blanco"),Checker("Blanco"),Checker("Blanco"),Checker("Blanco")],[],[],[],[],[Checker("Negro"),Checker("Negro")]
        ]
        juego.realizar_movimiento(0,2)
        self.assertEqual(len(juego.__board__.obtener_contenedor_fichas()[0]),1)
        self.assertEqual(len(juego.__board__.obtener_contenedor_fichas()[2]),1)
        self.assertEqual(juego.__board__.obtener_contenedor_fichas()[2][0].obtener_color(),"Blanco")
        self.assertEqual(len(juego.obtener_dados_disponibles()),1)
    
    @patch('random.randint', side_effect=[3, 2])
    def test_realizar_moviemto_posicion_invalida(self,mock_randint):
        juego = BackgammonGame()
        juego.tirar_dados()
        juego.__board__.__contenedor_fichas__ =  [
            [Checker("Blanco"),Checker("Blanco")],[],[],[],[],[Checker("Negro"),Checker("Negro"),Checker("Negro"),Checker("Negro"),Checker("Negro")], [],[Checker("Negro"),Checker("Negro"),Checker("Negro")],[],[],[],[Checker("Blanco"),Checker("Blanco"),Checker("Blanco"),Checker("Blanco"),Checker("Blanco")],
            [Checker("Negro"),Checker("Negro"),Checker("Negro"),Checker("Negro"),Checker("Negro")],[],[],[],[Checker("Blanco"),Checker("Blanco"),Checker("Blanco")],[], [Checker("Blanco"),Checker("Blanco"),Checker("Blanco"),Checker("Blanco"),Checker("Blanco")],[],[],[],[],[Checker("Negro"),Checker("Negro")]
        ]
        with self.assertRaises(MovimientoInvalido):
            juego.realizar_movimiento(0,5)
    
    @patch('random.randint', side_effect=[3, 2])
    def test_realizar_moviemto_posicion_inicial_invalida(self,mock_randint):
        juego = BackgammonGame()
        juego.tirar_dados()
        juego.__board__.__contenedor_fichas__ =  [
            [Checker("Blanco"),Checker("Blanco")],[],[],[],[],[Checker("Negro"),Checker("Negro"),Checker("Negro"),Checker("Negro"),Checker("Negro")], [],[Checker("Negro"),Checker("Negro"),Checker("Negro")],[],[],[],[Checker("Blanco"),Checker("Blanco"),Checker("Blanco"),Checker("Blanco"),Checker("Blanco")],
            [Checker("Negro"),Checker("Negro"),Checker("Negro"),Checker("Negro"),Checker("Negro")],[],[],[],[Checker("Blanco"),Checker("Blanco"),Checker("Blanco")],[], [Checker("Blanco"),Checker("Blanco"),Checker("Blanco"),Checker("Blanco"),Checker("Blanco")],[],[],[],[],[Checker("Negro"),Checker("Negro")]
        ]
        with self.assertRaises(MovimientoInvalido):
            juego.realizar_movimiento(1,3)
    @patch('random.randint', side_effect=[3, 2])
    def test_realizar_moviemto_sacar_ficha(self,mock_randint):
        juego = BackgammonGame()
        juego.tirar_dados()
        juego.__board__.__contenedor_fichas__ =  [
            [],[],[],[],[],[Checker("Negro"),Checker("Negro"),Checker("Negro"),Checker("Negro"),Checker("Negro")], [],[Checker("Negro"),Checker("Negro"),Checker("Negro")],[],[],[],[],
            [Checker("Negro"),Checker("Negro"),Checker("Negro"),Checker("Negro"),Checker("Negro")],[],[],[],[],[], [Checker("Blanco"),Checker("Blanco"),Checker("Blanco"),Checker("Blanco"),Checker("Blanco")],[Checker("Blanco"),Checker("Blanco")],[Checker("Blanco"),Checker("Blanco"),Checker("Blanco"),Checker("Blanco"),Checker("Blanco")],[],[Checker("Blanco"),Checker("Blanco"),Checker("Blanco")],[Checker("Negro"),Checker("Negro")]
        ]
        juego.realizar_movimiento(19,24)
        self.assertEqual(len(juego.__board__.obtener_contenedor_blancas_sacadas()),1)
        self.assertEqual(juego.__board__.obtener_contenedor_blancas_sacadas()[0].obtener_color(),"Blanco")
    @patch('random.randint', side_effect=[3, 2])
    def test_realizar_moviemto_sacar_ficha_error(self,mock_randint):
        juego = BackgammonGame()
        juego.tirar_dados()
        juego.__board__.__contenedor_fichas__ =  [
            [Checker("Blanco")],[],[],[],[],[Checker("Negro"),Checker("Negro"),Checker("Negro"),Checker("Negro"),Checker("Negro")], [],[Checker("Negro"),Checker("Negro"),Checker("Negro")],[],[],[],[],
            [Checker("Negro"),Checker("Negro"),Checker("Negro"),Checker("Negro"),Checker("Negro")],[],[],[],[],[], [Checker("Blanco"),Checker("Blanco"),Checker("Blanco"),Checker("Blanco"),Checker("Blanco")],[Checker("Blanco"),Checker("Blanco")],[Checker("Blanco"),Checker("Blanco"),Checker("Blanco"),Checker("Blanco"),Checker("Blanco")],[],[Checker("Blanco"),Checker("Blanco")],[Checker("Negro"),Checker("Negro")]
        ]
        with self.assertRaises(MovimientoInvalido):
            juego.realizar_movimiento(19,24)
    
    @patch('random.randint', side_effect=[3, 2])
    def test_realizar_movimientos_cambio_de_turno(self,mock_randint):
        juego = BackgammonGame()
        juego.tirar_dados()
        juego.__board__.__contenedor_fichas__ =  [
            [Checker("Blanco"),Checker("Blanco")],[],[],[],[],[Checker("Negro"),Checker("Negro"),Checker("Negro"),Checker("Negro"),Checker("Negro")], [],[Checker("Negro"),Checker("Negro"),Checker("Negro")],[],[],[],[Checker("Blanco"),Checker("Blanco"),Checker("Blanco"),Checker("Blanco"),Checker("Blanco")],
            [Checker("Negro"),Checker("Negro"),Checker("Negro"),Checker("Negro"),Checker("Negro")],[],[],[],[Checker("Blanco"),Checker("Blanco"),Checker("Blanco")],[], [Checker("Blanco"),Checker("Blanco"),Checker("Blanco"),Checker("Blanco"),Checker("Blanco")],[],[],[],[],[Checker("Negro"),Checker("Negro")]
        ]
        juego.realizar_movimiento(0,2)
        self.assertEqual(len(juego.__board__.obtener_contenedor_fichas()[0]),1)
        self.assertEqual(len(juego.__board__.obtener_contenedor_fichas()[2]),1)
        self.assertEqual(juego.__board__.obtener_contenedor_fichas()[2][0].obtener_color(),"Blanco")
        self.assertEqual(len(juego.obtener_dados_disponibles()),1)
        juego.realizar_movimiento(0,3)
        self.assertEqual(len(juego.__board__.obtener_contenedor_fichas()[0]),0)
        self.assertEqual(len(juego.__board__.obtener_contenedor_fichas()[3]),1)
        self.assertEqual(juego.__board__.obtener_contenedor_fichas()[3][0].obtener_color(),"Blanco")
        self.assertEqual(len(juego.obtener_dados_disponibles()),0)
        self.assertEqual(juego.obtener_turno(),"Negro")
    
    @patch('random.randint', side_effect=[3, 2])
    def test_realizar_movimiento_dado_invalido(self,mock_randint):
        juego = BackgammonGame()
        juego.tirar_dados()
        juego.__board__.__contenedor_fichas__ =  [
            [Checker("Blanco"),Checker("Blanco")],[],[],[],[],[Checker("Negro"),Checker("Negro"),Checker("Negro"),Checker("Negro"),Checker("Negro")], [],[Checker("Negro"),Checker("Negro"),Checker("Negro")],[],[],[],[Checker("Blanco"),Checker("Blanco"),Checker("Blanco"),Checker("Blanco"),Checker("Blanco")],
            [Checker("Negro"),Checker("Negro"),Checker("Negro"),Checker("Negro"),Checker("Negro")],[],[],[],[Checker("Blanco"),Checker("Blanco"),Checker("Blanco")],[], [Checker("Blanco"),Checker("Blanco"),Checker("Blanco"),Checker("Blanco"),Checker("Blanco")],[],[],[],[],[Checker("Negro"),Checker("Negro")]
        ]
        with self.assertRaises(MovimientoInvalido):
            juego.realizar_movimiento(0,4)
    
    @patch('random.randint', side_effect=[3, 2])
    def test_realizar_movimiento_desde_inicio(self,mock_randint):
        juego = BackgammonGame()
        juego.tirar_dados()
        juego.__board__.__contenedor_fichas__ =  [
            [Checker("Blanco")],[],[],[],[],[Checker("Negro"),Checker("Negro"),Checker("Negro"),Checker("Negro"),Checker("Negro")], [],[Checker("Negro"),Checker("Negro"),Checker("Negro")],[],[],[],[Checker("Blanco"),Checker("Blanco"),Checker("Blanco"),Checker("Blanco"),Checker("Blanco")],
            [Checker("Negro"),Checker("Negro"),Checker("Negro"),Checker("Negro"),Checker("Negro")],[],[],[],[Checker("Blanco"),Checker("Blanco"),Checker("Blanco")],[], [Checker("Blanco"),Checker("Blanco"),Checker("Blanco"),Checker("Blanco"),Checker("Blanco")],[],[],[],[],[Checker("Negro"),Checker("Negro")]
        ]
        juego.__board__.__contenedor_fichas_blancas__ = [Checker("Blanco")]
        juego.realizar_moviento_desde_inicio(2)
        self.assertEqual(len(juego.__board__.obtener_contenedor_fichas()[2]),1)
        self.assertEqual(len(juego.__board__.obtener_contenedor_blancas()),0)
        self.assertEqual(juego.__board__.obtener_contenedor_fichas()[2][0].obtener_color(),"Blanco")
        self.assertEqual(len(juego.obtener_dados_disponibles()),1)
    
    @patch('random.randint', side_effect=[3, 2])
    def test_realizar_movimiento_desde_inicio_cambio_turno(self,mock_randint):
        juego = BackgammonGame()
        juego.tirar_dados()
        juego.__board__.__contenedor_fichas__ =  [
            [],[],[],[],[],[Checker("Negro"),Checker("Negro"),Checker("Negro"),Checker("Negro"),Checker("Negro")], [],[Checker("Negro"),Checker("Negro"),Checker("Negro")],[],[],[],[Checker("Blanco"),Checker("Blanco"),Checker("Blanco"),Checker("Blanco"),Checker("Blanco")],
            [Checker("Negro"),Checker("Negro"),Checker("Negro"),Checker("Negro"),Checker("Negro")],[],[],[],[Checker("Blanco"),Checker("Blanco"),Checker("Blanco")],[], [Checker("Blanco"),Checker("Blanco"),Checker("Blanco"),Checker("Blanco"),Checker("Blanco")],[],[],[],[],[Checker("Negro"),Checker("Negro")]
        ]
        juego.__board__.__contenedor_fichas_blancas__ = [Checker("Blanco"),Checker("Blanco")]
        juego.realizar_moviento_desde_inicio(2)
        self.assertEqual(len(juego.__board__.obtener_contenedor_fichas()[2]),1)
        self.assertEqual(len(juego.__board__.obtener_contenedor_blancas()),1)
        self.assertEqual(juego.__board__.obtener_contenedor_fichas()[2][0].obtener_color(),"Blanco")
        self.assertEqual(len(juego.obtener_dados_disponibles()),1)
        juego.realizar_moviento_desde_inicio(1)
        self.assertEqual(len(juego.__board__.obtener_contenedor_fichas()[1]),1)
        self.assertEqual(len(juego.__board__.obtener_contenedor_blancas()),0)
        self.assertEqual(juego.__board__.obtener_contenedor_fichas()[1][0].obtener_color(),"Blanco")
        self.assertEqual(len(juego.obtener_dados_disponibles()),0)
        self.assertEqual(juego.obtener_turno(),"Negro")
    
    @patch('random.randint', side_effect=[5,2])
    def test_realizar_movimiento_desde_inicio_pos_invalida(self,mock_randint):
        juego = BackgammonGame()
        juego.tirar_dados()
        juego.__board__.__contenedor_fichas__ =  [
            [],[],[],[],[],[Checker("Negro"),Checker("Negro"),Checker("Negro"),Checker("Negro"),Checker("Negro")], [],[Checker("Negro"),Checker("Negro"),Checker("Negro")],[],[],[],[Checker("Blanco"),Checker("Blanco"),Checker("Blanco"),Checker("Blanco"),Checker("Blanco")],
            [Checker("Negro"),Checker("Negro"),Checker("Negro"),Checker("Negro"),Checker("Negro")],[],[],[],[Checker("Blanco"),Checker("Blanco"),Checker("Blanco")],[], [Checker("Blanco"),Checker("Blanco"),Checker("Blanco"),Checker("Blanco"),Checker("Blanco")],[],[],[],[],[Checker("Negro"),Checker("Negro")]
        ]
        juego.__board__.__contenedor_fichas_blancas__ = [Checker("Blanco"),Checker("Blanco")]
        with self.assertRaises(MovimientoInvalido):
            juego.realizar_moviento_desde_inicio(5)
    
    @patch('random.randint', side_effect=[3,2])
    def test_realizar_movimiento_desde_inicio_dado_no_coincide(self,mock_randint):
        juego = BackgammonGame()
        juego.tirar_dados()
        juego.__board__.__contenedor_fichas__ =  [
            [],[],[],[],[],[Checker("Negro"),Checker("Negro"),Checker("Negro"),Checker("Negro"),Checker("Negro")], [],[Checker("Negro"),Checker("Negro"),Checker("Negro")],[],[],[],[Checker("Blanco"),Checker("Blanco"),Checker("Blanco"),Checker("Blanco"),Checker("Blanco")],
            [Checker("Negro"),Checker("Negro"),Checker("Negro"),Checker("Negro"),Checker("Negro")],[],[],[],[Checker("Blanco"),Checker("Blanco"),Checker("Blanco")],[], [Checker("Blanco"),Checker("Blanco"),Checker("Blanco"),Checker("Blanco"),Checker("Blanco")],[],[],[],[],[Checker("Negro"),Checker("Negro")]
        ]
        juego.__board__.__contenedor_fichas_blancas__ = [Checker("Blanco"),Checker("Blanco")]
        with self.assertRaises(MovimientoInvalido):
            juego.realizar_moviento_desde_inicio(3)
    
    @patch('random.randint', side_effect=[3, 2])
    def test_realizar_movimiento_desde_inicio_come_ficha(self,mock_randint):
        juego = BackgammonGame()
        juego.tirar_dados()
        juego.__board__.__contenedor_fichas__ =  [
            [Checker("Blanco")],[],[Checker("Negro")],[],[],[Checker("Negro"),Checker("Negro"),Checker("Negro"),Checker("Negro")], [],[Checker("Negro"),Checker("Negro"),Checker("Negro")],[],[],[],[Checker("Blanco"),Checker("Blanco"),Checker("Blanco"),Checker("Blanco"),Checker("Blanco")],
            [Checker("Negro"),Checker("Negro"),Checker("Negro"),Checker("Negro"),Checker("Negro")],[],[],[],[Checker("Blanco"),Checker("Blanco"),Checker("Blanco")],[], [Checker("Blanco"),Checker("Blanco"),Checker("Blanco"),Checker("Blanco"),Checker("Blanco")],[],[],[],[],[Checker("Negro"),Checker("Negro")]
        ]
        juego.__board__.__contenedor_fichas_blancas__ = [Checker("Blanco")]
        juego.realizar_moviento_desde_inicio(2)
        self.assertEqual(len(juego.__board__.obtener_contenedor_fichas()[2]),1)
        self.assertEqual(len(juego.__board__.obtener_contenedor_blancas()),0)
        self.assertEqual(juego.__board__.obtener_contenedor_fichas()[2][0].obtener_color(),"Blanco")
        self.assertEqual(len(juego.obtener_dados_disponibles()),1)
        self.assertEqual(len(juego.__board__.obtener_contenedor_negras()),1)
        self.assertEqual(juego.__board__.obtener_contenedor_negras()[0].obtener_color(),"Negro")
    
    def test_quitar_ficha_comida(self):
        juego = BackgammonGame()
        juego.__board__.__contenedor_fichas_blancas__ = [Checker("Blanco")]
        juego.__board__.quitar_ficha_comida(juego.obtener_turno())
        self.assertEqual(len(juego.__board__.obtener_contenedor_blancas()),0)
    
    def test_quitar_ficha_comida_tunrno_negro(self):
        juego = BackgammonGame()
        juego.cambiar_turno()
        juego.__board__.__contenedor_fichas_negras__ = [Checker("Negras")]
        juego.__board__.quitar_ficha_comida(juego.obtener_turno())
        self.assertEqual(len(juego.__board__.obtener_contenedor_negras()),0)

