# ChangeLog

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