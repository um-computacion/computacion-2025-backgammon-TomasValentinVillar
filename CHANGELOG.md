# ChangeLog

## 2025-10-28

### Added

- test_puede_sacar_ficha_blanca_dado_mayor
- test_no_puede_sacar_blanca_sin_dado_valido
- test_puede_sacar_ficha_negra_dado_exacto
- test_puede_sacar_ficha_negra_dado_mayor
- test_no_puede_sacar_negra_fichas_fuera_home
- test_tiene_fichas_comidas_false
- test_todas_fichas_en_home_board_negras_true
- test_todas_fichas_en_home_board_negras_false

## 2025-10-26 (23:18)

### Changed

- test test_verificar_movimientos_posibles en test_backgammongame.py
- test test_verificar_movimientos_posibles_desde_inicio en test_backgammongame.py
- test test_verificar_movimientos_posibles_desde_inicio_negro en test_backgammongame.py
- test test_verificar_movimientos_posibles_negro en test_backgammongame.py

### Deleted

- test test_usar_dados_combinados en test_dice_manager.py
- test test_verificar_movimientos_y_dados_blanco_doble 
- test test_verificar_movimientos_y_dados_negro_doble

### Changed

- función verificar_movimientos_y_dados
- función _hay_movimientos_desde_inicio en clase MoceCalculator
- función _hay_movimientos_normales en clase MoceCalculator

## 2025-10-26 (20:20)

### Changed

- función verificar_movimientos_y_dados
- función _hay_movimientos_desde_inicio en clase MoceCalculator
- función _hay_movimientos_normales en clase MoceCalculator

### Deleted

- función usar_dados_combiandos()

## 2025-10-26

### Changed

- función _hay_movimietos_desde_inicio en clase MoveCalculator
- función verificar_movimientos_y_dados en clase BackgammonGame
- función usar_dados_combinados en clase DiceManager

## 2025-10-25

### Changed

- función main en pygameui.py
- función render_bear_off_zones en pygame.py
- función hittest_bear_off en pygame.py

## 2025-10-24

### Changed

- función _es_movimiento_valido en clase MoveCalculater
- test test_verificar_moviemtos_posibles_solo_sacar en test_backgammongame

## 2025-10-22

### Changed

- función _es_movimiento_valido en clase MoveCalculater
- función puede_sacar_ficha en clase RuleValidator
- función _puede_sacar_ficha_blanca en clase RuleValidator
- función _puede_sacar_ficha_negra en clase RuleValidator
- función realizar_movimiento en clase BackgammonGame
- función verificar_sacar_ficha en en clase BackgammonGame

### To DO

- que pase el test_verificar_moviemtos_posibles_solo_sacar 

## 2025-10-20

### Changed

- función main en pygameui.py

### Added

- función hit_test_bear_off en pygameuy.py
- función render_bear_off_zones en pygameuy.py
- función puede_empezar_bear_off en pygameuy.py


## 2025-10-19

### Changed

- función main en pygameui.py

### Added

- función render_captured_pieces en pygameuy.py
- función hit_test_captured

## 2025-10-18 (19:24)

### Changed

- función render_board en pygameui.py
- función main en pygameui.py

### To Do

- que funcione corrextamente la lógica para comer fichas

## 2025-10-18 

### Added

- archivo board_adapter en directorio pygame_ui

### Changed

- archivo pygameui.py en directorio pygame_ui

### Deleted

- archivo colors.py en pygame_ui

## 2025-10-12 (23:24)

### Added

- archivo colors.py en pygame_ui
- archivo __init__.py en pygame_ui
- clase BackgammonUI en pygameui.py

## 2025-10-12

### Changed

- corrijo el archivo move_calculator.py y cli py para aumentar la nota del pylint
- agrego dos líneas en .pylintrc para que pylint reconozca los imports en los archivos
- corrijo el github/workflows/ci.yml para que se muestre correctamente en github

## 2025-10-11

### Changed

- corrijo el archivos backgammongame.py, board.py, dice_manager.py, move_validator.py, rule_validator.py, checker.py, dice.py y player.py
- el puntaje de pylint pasó de 5 aprox a 8 aprox

## 2025-10-10

### Changed

- corrijo el archivo backgammongame.py para mejorar la de pylint (pasó 1 aproximadamente a 6,61 y 
    y el directorio core paso de 1 aproximadamente a 5)
- muevo los test a un directorio distinto exclisvo para los test

## 2025-10-9

### Added

- archivo test_dice_manager.py con los test de clase DiceManager
- archivo test_rule_validator.py con los test de clase RuleValidator
- archivo test_move_validator.py con los test de clase MoveValidator
- archivo test_move_calculator.py con los test de clase MoveCalculator

## 2025-10-8 (17:45)

### Added

- archivos test_checker.py en core
- archivos test_player.py en core
- test_obtener_nombre en test_player
- test_obtener_estado en test_player
- test_obtener_ficha en test_player
- test_definir_ganador en test_player
- test_definir_perdedor en test_player
- test_tirar_dado en test_dice
- tesst_obtener_color en test_checker

### Changed

- funcion __init__ en clase BackgammonGame
- función tirar_dados clase BackgammonGame
- función verificar_movimientos_y_dados clase BackgammonGame
- función obtener_dados_dispnibles clase BackgammonGame
- test_cantidad_mov en test_backgammongame
- test_cantidad_mov_iguales en test_backgammongame
- test_verificar_movimientos_y_dados_blanco en test_backgammongame
- test_verificar_movimientos_y_dados_blanco_doble en test_backgammongame
- test_verificar_movimientos_y_dados_negro en test_backgammongame
- test_verificar_movimientos_y_dados_negro_doble en test_backgammongame
- test_verificar_movimientos_y_dados_error en test_backgammongame
- test_varificar_cambio_turno_cambia en test_backgammongame

### Deleted

- atributo __dado_disponibles__ de BackgammonGame

## 2025-10-8

### Added

- archivos test_board.py en core
- archivos test_dice.py en core
- test__get_symbol_w en test_board
- test__get_symbol_B en test_board

### Changed

- muevo los test de board desde test_backgammongame a test_board
- muevo los test de dice desde test_backgammongame a test_dice

## 2025-10-5 (16:53)

### Added

- clase MoveCalculator en core/services/move_calculator

### Changed

- funcion  verificar_movimientos_posibles en clase BackgammonGame
- función __init__ en clase BackgammonGame
- función obtener_dados_disponibles en clase BackgammonGmae

### Deleted

- Excepción PosNoDisponibles (nunca fue usada)

## 2025-10-5

### Added

- clase DiceManager en core/services/dice_manager

### Changed

- funcion  verificar_movimientos_y_dados en clase BackgammonGame
- función tirar_dados en clase BackgammonGame
- función obtener_dados_disponibles en clase BackgammonGmae

## 2025-10-3 (10:22)

### Added

- clase Rule_Validator en core/rule_validator

### Changed

- funcion verificar_sacar_ficha en clase BackgammonGame

## 2025-10-3

### Added

- carpetas models, services y validators en core
- archivos dice_manager.py y move_calculator.py en serivces
- archivos move_validator.py y rule_validator.py en serivces

### Changed

- se ha movido los archivos dice.py, player.py y checker.py a la carpeta models
- funcion __init__ en clase BackgammonGame
- funcion verificar_posicion_disponible en clase BackgammonGame

## 2025-10-1


### Added

- funcion obtener_cantidad_de_fichas_comidas en clase Board
- test_verificar_movimientos_posibles en test
- test_obtener_cantidad_de_fichas_comidas en test
- test_obtener_cantidad_de_fichas_comidas_negro en test

### Changed
- funcion ejecutar en CLI
- funcion realizar_movimiento en clase BackgammonGame
- funcion tirar_dados en clase BackgammonGame
- funcion verificar_ficha en clase BackgammonGame
- funcion verificar_movimientos_y_dados 
- test_sacar_ficha en test
- test_sacar_ficha_negro en test
- test_realizar_movimiento_sacar_ficha en test

## 2025-9-28 (18:00)

### Added

- funcion verificar_ficha_comida en Board
- test test_verificar_movimientos_posibles_desde_inicio en test
- test test_verificar_movimientos_posibles_desde_inicio_no_hay en test
- test test_verificar_movimientos_posibles_desde_inicio_negro en test
- test test_verificar_movimientos_posibles_desde_inicio_negro_no_hay en test
- test test_verificar_ficha_comida en test
- test test_verificar_ficha_comida_no_hay en test
- test test_verificar_ficha_comida_negra en test
- test test_verificar_ficha_comida_negra_no_hay en test

### Changed
- funcion verificar_movimientos_posibles en BackgammonGame

## 2025-9-28

### Added

- Clase CLI
- funcion mostrar_tablero en CLI
- funcion inicializar_tablero en Board
- funcion inicializar_board en BackgammonGame
- test inicializar_board en test
- funcion obtener_board en BackgammonGame

## 2025-9-27

### Added

- funcion draw_full_board en clase Board
- funcion test_draw_full_board en test

## 2025-9-24 (13:33)

### Added

- funcion definir_ganador en clase Player
- funcion definir_perdedor en clase Player
- funcion verificarg_ganador_y_perdedor
- test test_verificar_ganador_y_perdedor_gana_blanco en test
- test test_verificar_ganador_y_perdedor_gana_negro en test
- test test_realizar_moviento_gana en test
- test test_realizar_moviento_gana_negro en test
- test test_realizar_movimiento_desde_inicio_dado_no_coincide en test
- test test_realizar_movimiento_desde_inicio_come_ficha en test
- test test_quitar_ficha_comida en test
- test test_quitar_ficha_comida_turno_negro en test

### Changed
- funcion realizar moviento en clase BackgammonGame

## 2025-9-24

### Added

- test ocupar_casilla_come_ficha en test
- test test_realizar_movimiento_desde_inicio en test
- test est_realizar_movimiento_desde_inicio_cambio_turno en test
- test test_realizar_movimiento_desde_inicio_pos_invalida en test
- test test_realizar_movimiento_desde_inicio_dado_no_coincide en test
- test test_realizar_movimiento_desde_inicio_come_ficha en test
- test test_quitar_ficha_comida en test
- test test_quitar_ficha_comida_turno_negro en test

## 2025-9-23

### Added
  - funcion obtener_dados_disponibles
  - funcion obtener_turno
  - test test_realizar_moviemto_posicion_invalida en test
  - test test_realizar_moviemto_posicion_inicial_invalida en test
  - test test_realizar_moviemto_sacar_ficha en test
  - test test_realizar_moviemto_sacar_ficha_error en test
  - test test_realizar_moviemtos_cambio_de_turno en test
  - test test_realizar_movimiento_dado_invalido en test

### Changed
  - funcion realizar_moviento en Clase BackgammonGame

## 2025-9-21 (23:12)

### Added
  - funcion quitar_ficha_comida en clase Board
  - funcion realizar_movimiento_desde_el_inicio en clase BackgammonGame 
  - funcion cambiar_turno en clase BackgammonGame
  - test cambio_de_turno_blanco en test
  - test cambio_de_turno_negro en test

### Changed
  - funcion verificar_cambio_de_turno en clase BackgammnoGame
  - funcion ocupar_casilla en clase BackgammonGame
  - funcion realizar_movimiento en clase BackgammmonGame

## 2025-9-21 (21:02)

### Added
  - funcion realizar movimiento en clase BackgammonGame
  - funcion obtener contenedor fichas
  - test realizar moviemiento en test

## 2025-9-21

### Added
  - archivo ci.yml en github/workflows
  - pylintrc

## Changed
  - requirements.txt

## 2025-9-20

### Added
  - funcion verficar_fichas_sacadas_15 en clase Boaed
  - test test_verficar_fichas_sacadas_15_negro en test
  - test test_verficar_fichas_sacadas_15_blanco en test

## 2025-9-20

### Added
  - clase player con core/player.py
  - funcion __init__ en clase Player
  - funciones para obtener atributos de clase Player
  - funcion crear jugador en clase BlackgammonGame
  - test test_crear_jugador en test

## 2025-9-14

### Added
  - Funcion verificar_cambio_turno en BackgammonGame
  - test  test_varificar_cambio_turno_cambia en test
  - test  test_varificar_cambio_turno_no_cambia test

## 2025-9-13 (19:47)

### Added
  - Funcion sacar_ficha en clase Board
  - test sacar_ficha_blanca en test
  - test sacar_ficha_negra en test

## 2025-9-13 (18:35)

### Added
  - Funcion comer_ficha en clase Board
  - test comer_ficha_negra en test
  - test comer_ficha_blanca en test

### Changed
  - Función __init__ de la Clase Board


## 2025-9-13

### Changed
  - Función verificar_movimientos_posibles de la Clase BackgammonGame
  - test verificar_movimientos_posibles en test
  - test verificar_movimientos_posibles_no_hay en test
  - test verificar_movimientos_posibles_negro en test
  - test verificar_movimientos_posibles_negro_no_hay en test

## 2025-9-10

### Changed
  - Función verificar_movimientos_y_dados de la Clase BackgammonGame
  - test verificar_movimientos_y_dados_blanco en test
  - test verificar_movimientos_y_dados_blanco_doble en test
  - test verificar_movimientos_y_dados_negro en test
  - test verificar_movimientos_y_dados_negro_doble en test
  - test verificar_movimientos_y_dados_error en test

## 2025-9-9 (23:06)

### Changed
  - Función verificar_movimientos_y_dados de la Clase BackgammonGame
  -

### Added
  - test verificar_movimientos_y_dados_blanco en test
  - test verificar_movimientos_y_dados_blanco_doble en test
  - test verificar_movimientos_y_dados_negro en test
  - test verificar_movimientos_y_dados_negro_doble en test
  - test verificar_movimientos_y_dados_error en test

## 2025-9-9 (21:18)

### Added
  - funcion verificar_moviemientos_y_dados en Clase BackgammonGame

## 2025-9-9

### Changed
  - Función tirar_dados de la Clase BackgammonGame
  - __init__ de clase Bakgammon

### Added
  - test test_cantidad_mov_iguales en test
  - test test_cantidad_mov en test

## 2025-9-8

### Changed
  - Función verificar_sacar_ficha de la Clase BackgammonGame

### Added
  - test test_sacar_ficha_error_negro en test
  - test test_sacar_ficha_negro en test

## 2025-9-4

### Added
  - test test_tirar_dados_diferentes en test
  - test test_tirar_dados_iguales en test

## 2025-8-31

### Changed
  - Función verificar_movimientos_posibles de la Clase BackgammonGame 

### Added
  - test test_verificar_movimientos_posibles_no_hay_negro en test
  - test test_verificar_movimientos_posibles_no_hay_negro en test

## 2025-8-30

### Changed
  - Función ocupar_casilla de la Clase BackgammonGame 

### Added
  - test comer_ficha en test

## 2025-8-29

### Added
  - Función verificar_sacar_ficha de la clase BackgammonGame
  - test de la función verificar_sacar_ficha 

## 2025-8-28

### Changed
  - Función verificar_moviemitos_posibles de la Clase BackgammonGame 
  - test de la funcion verificar_moviemitos_posibles
  - Función verificar_posicion_disponible de la Clase BackgammonGame 
  - test de la funcion verificar_posicion_disponible

## 2025-8-27

### Added
  - Información al Archivo CHANGELOG.md
  - La Clase Checker

## 2025-8-27 (23:16hs)

### Added
  - Función verificar_moviemitos_posibles de la Clase BackgammonGame (los test no pasan, se debe corregir)
  - test de la funcion verificar_moviemitos_posibles

## 2025-8-27

### Added
  - Información al Archivo CHANGELOG.md
  - La Clase Checker

### Changed
  - El atributo __conenedor_ficha__ de la Clase Board
  - La funcion quitar_ficha de la Clase Board
  - La funcion poner_ficha de la Clase Board
  - La funcion ocupar_casilla de la Clase BackgammonGame
  - La funcion verificar_posicion_disponible de la Clase BackgammonGame
  - Los test de quitar_ficha, poner_ficha , ocupar_casilla, verificar_posicion_disponible