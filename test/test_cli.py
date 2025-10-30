# tests/test_cli.py
import unittest
from unittest.mock import patch, MagicMock
from cli.cli import CLI
from core.backgammongame import (
    MovimientoInvalido, 
    NoHayMovimientosPosibles, 
    Ganador,
    NoSeIngresoEnteroError
)
from core.models.dice import Dice


class TestCLI(unittest.TestCase):
    
    # ═══════════════════════════════════════════════════════════════
    # CAMINO 1: IF - Jugador tiene fichas comidas
    # ═══════════════════════════════════════════════════════════════
    
    @patch('builtins.print')
    @patch('builtins.input', side_effect=[
        'Jugador1',  # Nombre jugador 1
        'Jugador2',  # Nombre jugador 2
        '5',         # Posición final para ficha comida
    ])
    @patch.object(CLI, 'mostrar_tablero')
    def test_camino_if_ficha_comida(self, mock_tablero, mock_input, mock_print):
        """
        CAMINO 1: IF - Tiene fichas comidas, debe llamar realizar_moviento_desde_inicio()
        """
        cli = CLI()
        
        # Crear dados mockeados
        dado_mock = MagicMock(spec=Dice)
        dado_mock.obtener_numero.return_value = 3
        
        # Mockear métodos del juego
        cli.__juego__.obtener_board().verificar_ficha_comida = MagicMock(return_value=True)
        cli.__juego__.obtener_board().obtener_cantidad_de_fichas_comidas = MagicMock(return_value=1)
        cli.__juego__.obtener_dados_disponibles = MagicMock(return_value=[dado_mock])
        cli.__juego__.verifificar_movimientos_posibles = MagicMock(return_value=True)
        cli.__juego__.obtener_turno = MagicMock(return_value='Blanco')
        cli.__juego__.obtener_players = MagicMock(return_value={
            'Blanco': MagicMock(obtener_nombre=MagicMock(return_value='Jugador1'))
        })
        cli.__juego__.realizar_moviento_desde_inicio = MagicMock(
            side_effect=Ganador("Ganaste!")
        )
        cli.__juego__.tirar_dados = MagicMock()
        
        # Ejecutar
        cli.ejecutar()
        
        # Verificar que se llamó realizar_moviento_desde_inicio
        cli.__juego__.realizar_moviento_desde_inicio.assert_called_once_with(5)
    
    # ═══════════════════════════════════════════════════════════════
    # CAMINO 2: ELSE - Jugador NO tiene fichas comidas
    # ═══════════════════════════════════════════════════════════════
    
    @patch('builtins.print')
    @patch('builtins.input', side_effect=[
        'Jugador1',
        'Jugador2',
        '10',
        '15',
    ])
    @patch.object(CLI, 'mostrar_tablero')
    def test_camino_else_sin_fichas_comidas(self, mock_tablero, mock_input, mock_print):
        """
        CAMINO 2: ELSE - NO tiene fichas comidas, debe llamar realizar_movimiento()
        """
        cli = CLI()
        
        dado_mock = MagicMock(spec=Dice)
        dado_mock.obtener_numero.return_value = 5
        
        cli.__juego__.obtener_board().verificar_ficha_comida = MagicMock(return_value=False)
        cli.__juego__.obtener_dados_disponibles = MagicMock(return_value=[dado_mock])
        cli.__juego__.verifificar_movimientos_posibles = MagicMock(return_value=True)
        cli.__juego__.obtener_turno = MagicMock(return_value='Blanco')
        cli.__juego__.obtener_players = MagicMock(return_value={
            'Blanco': MagicMock(obtener_nombre=MagicMock(return_value='Jugador1'))
        })
        cli.__juego__.combertir_entero = MagicMock(side_effect=[10, 15])
        cli.__juego__.realizar_movimiento = MagicMock(
            side_effect=Ganador("Ganaste!")
        )
        cli.__juego__.tirar_dados = MagicMock()
        
        # Ejecutar
        cli.ejecutar()
        
        # Verificar que se llamó realizar_movimiento
        cli.__juego__.realizar_movimiento.assert_called_once_with(10, 15)
    
    # ═══════════════════════════════════════════════════════════════
    # CAMINO 3: Excepción MovimientoInvalido
    # ═══════════════════════════════════════════════════════════════
    
    @patch('builtins.print')
    @patch('builtins.input', side_effect=[
        'Jugador1',
        'Jugador2',
        '10',
        '15',
        '11',
        '16',
    ])
    @patch.object(CLI, 'mostrar_tablero')
    def test_excepcion_movimiento_invalido(self, mock_tablero, mock_input, mock_print):
        """
        CAMINO 3: Excepción MovimientoInvalido - Debe capturar y mostrar el error
        """
        cli = CLI()
        
        dado_mock = MagicMock(spec=Dice)
        dado_mock.obtener_numero.return_value = 5
        
        cli.__juego__.obtener_board().verificar_ficha_comida = MagicMock(return_value=False)
        cli.__juego__.obtener_dados_disponibles = MagicMock(return_value=[dado_mock])
        cli.__juego__.verifificar_movimientos_posibles = MagicMock(return_value=True)
        cli.__juego__.obtener_turno = MagicMock(return_value='Blanco')
        cli.__juego__.obtener_players = MagicMock(return_value={
            'Blanco': MagicMock(obtener_nombre=MagicMock(return_value='Jugador1'))
        })
        cli.__juego__.combertir_entero = MagicMock(side_effect=[10, 15, 11, 16])
        cli.__juego__.realizar_movimiento = MagicMock(
            side_effect=[
                MovimientoInvalido("Movimiento no válido"),
                Ganador("Ganaste!")
            ]
        )
        cli.__juego__.tirar_dados = MagicMock()
        
        # Ejecutar
        cli.ejecutar()
        
        # Verificar que se imprimió el error
        error_printed = any(
            "Movimiento no válido" in str(call) 
            for call in mock_print.call_args_list
        )
        self.assertTrue(error_printed)
    
    # ═══════════════════════════════════════════════════════════════
    # CAMINO 4: Excepción NoSeIngresoEnteroError
    # ═══════════════════════════════════════════════════════════════
    
    @patch('builtins.print')
    @patch('builtins.input', side_effect=[
        'Jugador1',
        'Jugador2',
        'abc',
        '15',
    ])
    @patch.object(CLI, 'mostrar_tablero')
    def test_excepcion_no_se_ingreso_entero(self, mock_tablero, mock_input, mock_print):
        """
        CAMINO 4: Excepción NoSeIngresoEnteroError - Debe capturar error de input
        """
        cli = CLI()
        
        dado_mock = MagicMock(spec=Dice)
        dado_mock.obtener_numero.return_value = 5
        
        cli.__juego__.obtener_board().verificar_ficha_comida = MagicMock(return_value=False)
        cli.__juego__.obtener_dados_disponibles = MagicMock(return_value=[dado_mock])
        cli.__juego__.verifificar_movimientos_posibles = MagicMock(return_value=True)
        cli.__juego__.obtener_turno = MagicMock(return_value='Blanco')
        cli.__juego__.obtener_players = MagicMock(return_value={
            'Blanco': MagicMock(obtener_nombre=MagicMock(return_value='Jugador1'))
        })
        cli.__juego__.combertir_entero = MagicMock(
            side_effect=[
                NoSeIngresoEnteroError("Debe ingresar un número"),
                Ganador("Ganaste!")
            ]
        )
        cli.__juego__.tirar_dados = MagicMock()
        
        # Ejecutar
        cli.ejecutar()
        
        # Verificar que se imprimió el error
        error_printed = any(
            "Debe ingresar un número" in str(call) 
            for call in mock_print.call_args_list
        )
        self.assertTrue(error_printed)
    
    # ═══════════════════════════════════════════════════════════════
    # CAMINO 5: Excepción NoHayMovimientosPosibles
    # ═══════════════════════════════════════════════════════════════
    
    @patch('builtins.print')
    @patch('builtins.input', side_effect=[
        'Jugador1',
        'Jugador2',
    ])
    @patch.object(CLI, 'mostrar_tablero')
    def test_excepcion_no_hay_movimientos(self, mock_tablero, mock_input, mock_print):
        """
        CAMINO 5: Excepción NoHayMovimientosPosibles - BackgammonGame cambia turno automáticamente
        El CLI solo captura la excepción e imprime el mensaje
        """
        cli = CLI()
        
        dado_mock = MagicMock(spec=Dice)
        dado_mock.obtener_numero.return_value = 5
        
        cli.__juego__.obtener_board().verificar_ficha_comida = MagicMock(return_value=False)
        cli.__juego__.obtener_dados_disponibles = MagicMock(return_value=[dado_mock])
        cli.__juego__.obtener_turno = MagicMock(return_value='Blanco')
        cli.__juego__.obtener_players = MagicMock(return_value={
            'Blanco': MagicMock(obtener_nombre=MagicMock(return_value='Jugador1'))
        })
        

        cli.__juego__.verifificar_movimientos_posibles = MagicMock(
            side_effect=[
                NoHayMovimientosPosibles("No hay movimientos"),
                Ganador("Ganaste!")
            ]
        )
        cli.__juego__.tirar_dados = MagicMock()
        
        # Ejecutar
        cli.ejecutar()
        
        # Verificar que se capturó e imprimió el mensaje de error
        error_printed = any(
            "movimiento" in str(call).lower()
            for call in mock_print.call_args_list
        )
        self.assertTrue(error_printed, "Debe imprimir el mensaje de NoHayMovimientosPosibles")
        
        # NO verificar cambiar_turno porque BackgammonGame ya lo hizo internamente

    # ═══════════════════════════════════════════════════════════════
    # CAMINO 6: Excepción Ganador
    # ═══════════════════════════════════════════════════════════════
    
    @patch('builtins.print')
    @patch('builtins.input', side_effect=[
        'Jugador1',
        'Jugador2',
        '10',
        '15',
    ])
    @patch.object(CLI, 'mostrar_tablero')
    def test_excepcion_ganador(self, mock_tablero, mock_input, mock_print):
        """
        CAMINO 6: Excepción Ganador - Debe mostrar mensaje de victoria y terminar
        """
        cli = CLI()
        
        dado_mock = MagicMock(spec=Dice)
        dado_mock.obtener_numero.return_value = 5
        
        cli.__juego__.obtener_board().verificar_ficha_comida = MagicMock(return_value=False)
        cli.__juego__.obtener_dados_disponibles = MagicMock(return_value=[dado_mock])
        cli.__juego__.verifificar_movimientos_posibles = MagicMock(return_value=True)
        cli.__juego__.obtener_turno = MagicMock(return_value='Blanco')
        cli.__juego__.obtener_players = MagicMock(return_value={
            'Blanco': MagicMock(obtener_nombre=MagicMock(return_value='Jugador1'))
        })
        cli.__juego__.combertir_entero = MagicMock(side_effect=[10, 15])
        cli.__juego__.realizar_movimiento = MagicMock(
            side_effect=Ganador("¡Ganaste la partida!")
        )
        cli.__juego__.tirar_dados = MagicMock()
        
        # Ejecutar
        cli.ejecutar()
        
        # Verificar que se mostró el mensaje de victoria
        victoria_printed = any(
            "Ganaste" in str(call) 
            for call in mock_print.call_args_list
        )
        self.assertTrue(victoria_printed)
        
        # Verificar que se llamó mostrar_tablero al final
        self.assertGreater(mock_tablero.call_count, 0)
    # ═══════════════════════════════════════════════════════════════
    # TEST ADICIONAL: Validación de nombres (NombreVacio)
    # ═══════════════════════════════════════════════════════════════
    
    @patch('builtins.print')
    @patch('builtins.input', side_effect=[
        '',           # nombre1 (vacío - causará NombreVacio)
        'Temporal',   # nombre2 (se pide pero no se usa por la excepción)
        'Jugador1',   # nombre1 (retry después del error)
        'Jugador2',   # nombre2 (retry exitoso)
        '10',         # pos_inic
        '15',         # pos_fin
    ])
    @patch.object(CLI, 'mostrar_tablero')
    def test_nombre_vacio_excepcion(self, mock_tablero, mock_input, mock_print):
        """
        TEST ADICIONAL: Excepción NombreVacio al ingresar nombre vacío
        Cubre líneas 20-43 (bucle de entrada de nombres con retry)
        Usa la validación REAL de crear_jugador()
        """
        cli = CLI()
        
        # NO mockear crear_jugador - usar la implementación real
        # que valida nombre vacío internamente
        
        dado_mock = MagicMock(spec=Dice)
        dado_mock.obtener_numero.return_value = 5
        
        # Mockear solo lo necesario para el juego
        cli.__juego__.obtener_board().verificar_ficha_comida = MagicMock(return_value=False)
        cli.__juego__.obtener_dados_disponibles = MagicMock(return_value=[dado_mock])
        cli.__juego__.verifificar_movimientos_posibles = MagicMock(return_value=True)
        cli.__juego__.obtener_turno = MagicMock(return_value='Blanco')
        cli.__juego__.obtener_players = MagicMock(return_value={
            'Blanco': MagicMock(obtener_nombre=MagicMock(return_value='Jugador1'))
        })
        cli.__juego__.combertir_entero = MagicMock(side_effect=[10, 15])
        cli.__juego__.realizar_movimiento = MagicMock(
            side_effect=Ganador("Ganaste!")
        )
        cli.__juego__.tirar_dados = MagicMock()
        
        # Ejecutar
        cli.ejecutar()
        
        # Verificar que se imprimió el error de nombre vacío
        error_printed = any(
            ("nombre" in str(call).lower() and "vacío" in str(call).lower()) or
            "vacío" in str(call)
            for call in mock_print.call_args_list
        )
        self.assertTrue(error_printed, "Debe imprimir error de nombre vacío")
    
    # ═══════════════════════════════════════════════════════════════
    # TEST ADICIONAL: Múltiples movimientos antes de cambiar turno
    # ═══════════════════════════════════════════════════════════════
    
    @patch('builtins.print')
    @patch('builtins.input', side_effect=[
        'Jugador1',
        'Jugador2',
        '10',
        '12',  # Primer movimiento
        '15',
        '18',  # Segundo movimiento
    ])
    @patch.object(CLI, 'mostrar_tablero')
    def test_multiples_movimientos_mismo_turno(self, mock_tablero, mock_input, mock_print):
        """
        TEST ADICIONAL: Hacer múltiples movimientos en el mismo turno
        Cubre las líneas donde se verifica si quedan dados disponibles
        """
        cli = CLI()
        
        dado_mock1 = MagicMock(spec=Dice)
        dado_mock1.obtener_numero.return_value = 2
        dado_mock2 = MagicMock(spec=Dice)
        dado_mock2.obtener_numero.return_value = 3
        
        cli.__juego__.obtener_board().verificar_ficha_comida = MagicMock(return_value=False)
        
        # Primera llamada: 2 dados, segunda: 1 dado, tercera: 0 dados
        cli.__juego__.obtener_dados_disponibles = MagicMock(
            side_effect=[
                [],  # Necesita tirar
                [dado_mock1, dado_mock2],  # Después de tirar
                [dado_mock1, dado_mock2],  # Mostrar dados
                [dado_mock2],  # Después del primer movimiento
                [dado_mock2],  # Mostrar dados restantes
                []  # Después del segundo movimiento
            ]
        )
        cli.__juego__.verifificar_movimientos_posibles = MagicMock(return_value=True)
        cli.__juego__.obtener_turno = MagicMock(return_value='Blanco')
        cli.__juego__.obtener_players = MagicMock(return_value={
            'Blanco': MagicMock(obtener_nombre=MagicMock(return_value='Jugador1'))
        })
        cli.__juego__.combertir_entero = MagicMock(side_effect=[10, 12, 15, 18])
        cli.__juego__.realizar_movimiento = MagicMock(
            side_effect=[None, Ganador("Ganaste!")]
        )
        cli.__juego__.tirar_dados = MagicMock()
        
        # Ejecutar
        cli.ejecutar()
        
        # Verificar que se realizaron 2 movimientos
        self.assertEqual(cli.__juego__.realizar_movimiento.call_count, 2)
    
    # ═══════════════════════════════════════════════════════════════
    # TEST ADICIONAL: mostrar_tablero()
    # ═══════════════════════════════════════════════════════════════
    
    @patch('builtins.print')
    def test_mostrar_tablero(self, mock_print):
        """
        TEST: mostrar_tablero() ejecuta prints y llama a draw_full_board()
        """
        cli = CLI()
        
        # Mockear draw_full_board para retornar un tablero simple
        tablero_mock = [
            ['W', 'W', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'B'],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['B', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'W'],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        ]
        
        cli.__juego__.obtener_board().draw_full_board = MagicMock(return_value=tablero_mock)
        
        # Ejecutar
        cli.mostrar_tablero()
        
        # Verificar que se llamó draw_full_board
        cli.__juego__.obtener_board().draw_full_board.assert_called_once()
        
        # Verificar que se hicieron prints (al menos los headers)
        self.assertGreater(mock_print.call_count, 0, "Debe hacer al menos un print")
        
        # Verificar que se imprimieron las posiciones
        prints_realizados = [str(call) for call in mock_print.call_args_list]
        headers_encontrados = any("Pos:" in p for p in prints_realizados)
        self.assertTrue(headers_encontrados, "Debe imprimir los headers de posiciones")



if __name__ == '__main__':
    unittest.main()
