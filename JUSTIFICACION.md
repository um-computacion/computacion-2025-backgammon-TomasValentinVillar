# Diseño General

El diseño del proyecto consiste en la parte principal del proyecto, que es el directorio core, donde se encuentra la logica de central del juego Backgammon. Para interactuar con el juego está la línea de comando (CLI) para jugar a traveź de la terminal y la otra forma de interactuar con el juego es atravez de gráficos con Pygame.

El el proyecto se encuentra el directorio test, donde están los test de cada una de las calses del proyecto incluyecdo el CLI, la covertura del código se realizó con pruebas unitarias

# Clases Elegidas

## Checker

Representa un ficha del tablero, tiene un unico atributo que es color, y sirve para identificar si la ficha es color o negro, al crear una instacia de Checker recibe el parametro el color correspondiente y tiene un metodo obtener_color() que retorna el atributo color de la ficha

## Dice

Representa un dado del tablero, su atributo es numero y esta clase utiliza random para definir el su numero correspondiente, es la clase responsable del dado y su valor

## Player

Es la clase utilizada para cada jugador, sus atributos son nombre, estado y ficha. El atributo ficha es color de la ficha correspondiente al jugador y el atributo estado define si el jugador está jugando, ganó o empató, (es una idea que saqué del trabajo práctico ta te ti). La responsabilidad de la clase es mantener la información de los jugadores del juego como la su color correspondiente en el juego (blanco o negro y su estado)

## Board

Esta clase define el tablero del juego. Es la que mantiene información de la posición de cada una de las fichas en el tablero, también tiene información de las fichas capturadas y de las fichas ya sacadas del tablero, esta clase es la que quita la fichas de una posición especioca y pone la ficha en otra posición especifica, valida si un jugador ganó, sabiendo si se quitaron las 15 fichas del tablero.

La reponsabilidad de Board es el estado de las fichas en juego 

## MoveValidator

Es la clase encargada de validar si un movimiento es legal, es decir que si el movimiento que se quiere realiazr es posible segun las reglas básicas, por ejemplo si el moviemito conicide con algun dado, si la posición no está ocupada por más de una ficha del oponente o acumular fichas en una posición. Por lo tanto su reonsabilidad es verifica si una posición está disponible para colocar una ficha

## RuleValidator

Es la clase encargada verificar las reglas especiales como sacar fichas del tablero y verificar (a travez de la clase tablero), lo que hcae ára verificar si se puede sacar una ficha segun el turno, todas las fichas deben estar en el home board (útimo cuadrante), El dado debe coincidir EXACTAMENTE con la distancia necesaria para sacar la ficha y Si el dado es MAYOR y NO hay fichas más atrás, se puede sacar. Entonces su reponsabilidad es vlidar reglas especiales del Backgammon

## DiceManager

Es la clase cuya reponsabilidad es gestionar los dados del juego, por lo tanto es la clase que sabe sobre los dados disponibles, puede utilizar dado para consumir un dado dsiponible, puede tirrar los dados para definir su valor y saber si se duplixan o nó, retorna información sobre los dados dsiponiles.

## CLI

Es la interfaz por linea de comando para jugar. Separar la interfaz de usuario de la lógica del juego. La funcionalidad del CLI es solicitar los nombres de jugadores, mostrar el tablero, capturar input del usuario, manejar excepciones y muestrar mensajes de error y controlar el flujo del juego

## MoveCalcualtor

Es la clase cuya responsabilidad es de calcular los movientos posibles, calcula si hay movimientos posibles desde inicio (ficha capturada) o si hay moviemitos normales posibles, tabién calcula distancioa entre dos posiciones, retorna True si hay al menos un movimiento posible.

- `move_validator`: utiliza la clase MoveValidator para verificar en cada una 
  de las posiciones ocupadas por fichas correspondientes al turno si se puede 
  realizar algún movimiento con los dados disponibles

- `rule_validator`: utiliza la clase RuleValidator para verificar si alguno 
  de los movimientos posibles es quitar una ficha del tablero (bear off)

## Clase BackgammonGame

Es la clase encargada de orquestar el juego Backgammon, utilizando a todas las clases anteriores. Se encarga de realizar los moviemtos del juego pasando por las validaciones necesarias, utiliza la información de los dados y del tablero para relizar los moviemitos y gestionar en turno de cada jugador, contiene las validacioens de para ganar o perder.


## Clase BoardAdapter

Es una clase que utilizo en pyagme para traducir el formato de la información de las fichas en cada posición del tablero, es decir que combierte la estructura de Checkers a tuplas, para que sea compatible con el formato de pygame propuesto en Slack.

Convierte: [Checker, Checker, ...] → ('white'/'black', cantidad)


# Justificación de Atributos

##  Atributos de `BackgammonGame`

### `__turno__: str`
**Justificación:** 
- Almacena qué jugador debe mover ("Blanco" o "Negro")
- Fundamental para validar movimientos (solo se pueden mover fichas del turno actual)
- Se alterna cuando se agotan los dados o no hay movimientos posibles

### `__board__: Board`
**Justificación:**
- Referencia al tablero del juego
- Permite acceder al estado de las fichas
- Se usa en prácticamente todos los movimientos

### `__move_validator__: MoveValidator`
**Justificación:**
- Servicio para validar movimientos básicos
- Inyección de dependencias (cumple DIP)
- Permite reemplazar con mock en tests

### `__rule_validator__: RuleValidator`
**Justificación:**
- Servicio para validar reglas especiales
- Inyección de dependencias
- Separación de responsabilidades

### `__dice_manager__: DiceManager`
**Justificación:**
- Gestiona toda la lógica de dados
- Centraliza el control de movimientos disponibles
- Facilita saber cuándo cambiar de turno

### `__move_calculator__: MoveCalculator`
**Justificación:**
- Calcula si hay movimientos posibles
- Evita duplicar lógica de verificación
- Permite cambiar turno automáticamente

### `__players__: dict`
**Justificación:**
- Diccionario con clave = color de ficha ("Blanco"/"Negro")
- Valor = instancia de `Player`
- Permite acceso rápido: `players[turno]`
- Idea tomada del proyecto Ta-Te-Ti

## Atributos de `Board`

### `__contenedor_fichas__: list[list[Checker]]`
**Justificación:**
- Lista de 24 listas (las 24 posiciones del tablero)
- Cada sublista contiene objetos `Checker`
- Permite apilar fichas en una posición: `contenedor_fichas[5] = [Checker("Blanco"), Checker("Blanco")]`
- **Ventaja:** Fácil de iterar y manipular

### `__contenedor_fichas_blancas_sacadas__: list[Checker]`
**Justificación:**
- Almacena fichas blancas que han completado el recorrido
- Condición de victoria: `len() == 15`
- Permite revertir movimiento si fuera necesario

### `__contenedor_fichas_negras_sacadas__: list[Checker]`
**Justificación:**
- Igual que el anterior pero para fichas negras
- Separación por color facilita verificación de victoria

### `__contenedor_fichas_blancas__: list[Checker]`
**Justificación:**
- Almacena fichas blancas capturadas por el oponente
- Si `len() > 0`, el jugador blanco DEBE meter fichas antes de mover otras
- Implementa la regla de Backgammon correctamente

### `__contenedor_fichas_negras__: list[Checker]`
**Justificación:**
- Igual que el anterior pero para fichas negras
- Separación por color simplifica la lógica

## Atributos de `DiceManager`

### `__dice1__: Dice`
**Justificación:**
- Primer dado del juego
- Instancia de la clase `Dice`
- Permite tirar y obtener valor

### `__dice2__: Dice`
**Justificación:**
- Segundo dado del juego
- Independiente del primero
- Backgammon siempre usa exactamente 2 dados

### `__dados_disponibles__: list[Dice]`
**Justificación:**
- Lista dinámica de dados que aún no se han usado en el turno
- Si dados son iguales: 4 elementos (dobles)
- Si dados son diferentes: 2 elementos
- Se vacía a medida que se hacen movimientos
- Cuando queda vacía → cambio de turno

## Atributos de `MoveCalculator`

### `__move_validator__: MoveValidator`
**Justificación:**
- Necesita validar si posiciones son disponibles
- Composición: `MoveCalculator` usa `MoveValidator`
- Evita duplicar código de validación

### `__rule_validator__: RuleValidator`
**Justificación:**
- Necesita verificar reglas especiales (ej: bear off)
- Composición: `MoveCalculator` usa `RuleValidator`
- Separación de responsabilidades

## Atributos de `BoardAdapter`

### `__backgammon_game__: BackgammonGame`
**Justificación:**
- Referencia al juego para obtener el estado del tablero
- Permite llamar a `backgammon_game.obtener_board()`
- Acceso al estado completo del juego

### `__pos__: dict`
**Justificación:**
- Diccionario con formato adaptado para Pygame
- Clave: índice de posición (0-23)
- Valor: tupla `(color, cantidad)` o `None`
- Formato que espera el renderizador de Pygame

## Atributos de Modelos

### `Checker.__color__: str`
**Justificación:**
- Único atributo necesario
- Identifica al dueño de la ficha
- Valores posibles: "Blanco" o "Negro"

### `Dice.__numero__: int`
**Justificación:**
- Valor del dado (1-6)
- Se actualiza al llamar `tirar_dado()`
- Se consulta con `obtener_numero()`

### `Player.__nombre__: str`
**Justificación:**
- Identificación del jugador
- Se muestra en mensajes y UI

### `Player.__ficha__: str`
**Justificación:**
- Color de ficha asignado ("Blanco" o "Negro")
- Determina qué fichas controla el jugador

### `Player.__estado__: str`
**Justificación:**
- Estado actual: "Jugando", "Ganador", "Perdedor"
- Permite determinar resultado al final del juego
- Idea tomada de Ta-Te-Ti

# Decisiones de Diseño generales

En un principio las clases DiceManager, MoveValidator, MoveCalculator y RuleValidator no exitían, todas esas responsabilidades las las tenía BackgammonGame, y para que se cumplan los principios SOLID dividí las reponsabilidades en esas clases.

También por cada commit se ha hecho actualizado el archivo CHANGELOG.md.

Los reportes del coverage y el pylint se generan automáticamente en una rama llamda automated-reports-update, en dicha ramma hay un archivo REPORTS.md donde se encuentran los reportes, y agregado promnts enviados a la IA utilizados para el desarrollo del proyecto

Para el puntaje del pylint, incluí a los directorios core, cli y pygame_ui. En un principio, antes de incluir al pygame tenpia un puntaje superior a 9 con el core y cli, pero despues de incluirlo ha bajado mucho el puntaje (8,5), y no he podido mejorarlo

Se han incluido los archivos de test en .coveragerc para coverage los ignore

También se ha decidido Usar `list[list[Checker]]` en lugar de diccionario o matriz, porque las posiciones son secuenciales (0-23), las listas permiten apilar fichas fácilmente, operaciones O(1) para acceso por índice y fácil de iterar con `for pos in range(24)`

Se han utilizado excepciones personalizadas para situaciones especiales del juego. Sirven para evitar retornar códigos de error, las excepciones se propagan automáticamente y el nombre de excepción explica qué pasó (`NoHayMovimientosPosibles`)

# Excepcioenes y manejo de errores

### Excepciones Personalizadas Definidas

#### `NoHayMovimientosPosibles`

**Cuándo se lanza:**
- Cuando `verifificar_movimientos_posibles()` determina que el jugador no puede hacer ningún movimiento válido con los dados actuales.

**Por qué es necesaria:**
- Situación normal en Backgammon (jugador bloqueado)
- No es un error del programa, es parte del juego
- Dispara cambio de turno automático

**Manejo:**
```python
try:
    juego.verifificar_movimientos_posibles()
except NoHayMovimientosPosibles as e:
    print(e)
    # El turno ya se cambió automáticamente en la función
```

**Ejemplo de situación:**
- Jugador tiene dados [3, 5]
- Todas las posiciones a 3 y 5 pasos están bloqueadas por el oponente
- No puede mover ninguna ficha

#### `MovimientoInvalido`

**Cuándo se lanza:**
- Cuando se intenta un movimiento que viola las reglas
- Posición inicial no tiene fichas del turno actual
- Posición destino está bloqueada (2+ fichas enemigas)
- El movimiento no coincide con ningún dado disponible
- Se intenta sacar ficha sin cumplir condiciones

**Por qué es necesaria:**
- Valida las reglas del juego
- Protege la integridad del estado del tablero
- Proporciona feedback claro al usuario

**Ejemplos de situaciones:**
```python
# Caso 1: Posición inicial inválida
board[pos_inic] = []  # Posición vacía
→ MovimientoInvalido("No se puede realizar ese movimiento")

# Caso 2: Posición bloqueada
board[pos_fin] = [Checker("Negro"), Checker("Negro")]  # 2+ fichas enemigas
→ MovimientoInvalido("No se puede realizar ese movimiento")

# Caso 3: Dado no coincide
dados_disponibles = [3, 5]
movimiento_de_7_pasos()
→ MovimientoInvalido("No hay dado disponible para 7 pasos")

# Caso 4: Bear off inválido
tiene_fichas_fuera_del_home_board = True
→ MovimientoInvalido("No se puede sacar ficha: hay fichas fuera del home board")
```

#### `Ganador`

**Cuándo se lanza:**
- Cuando un jugador saca su ficha #15 del tablero
- Se verifica en `verificar_ganador_y_perdedor()`
- Se lanza en `realizar_movimiento()` después de sacar ficha

**Por qué es necesaria:**
- Termina el juego inmediatamente
- Forma elegante de salir de loops anidados
- Idea tomada del proyecto Ta-Te-Ti

**Flujo de uso:**
```python
try:
    while True:  # Loop principal del juego
        juego.realizar_movimiento(pos_inic, pos_fin)
except Ganador as e:
    print(e)  # "¡Ganaste!"
    mostrar_pantalla_victoria()
    # Sale del loop automáticamente
```

**Ventajas sobre usar un flag:**
- No necesita verificar condición en cada iteración
- Sale de múltiples niveles de loops
- Código más limpio


#### `NombreVacio`

**Cuándo se lanza:**
- Al intentar crear un jugador con nombre vacío
- En `crear_jugador()` si `nom == ''`

**Por qué es necesaria:**
- Valida input del usuario
- Evita jugadores sin identificación
- Proporciona mensaje de error claro

**Manejo en CLI:**
```python
while True:
    try:
        nombre1 = input('Ingrese el nombre del jugador para las fichas Blancas: ')
        nombre2 = input('Ingrese el nombre del jugador para las fichas Negras: ')
        juego.crear_jugador(nombre1, 'Blanco', 'Jugando')
        juego.crear_jugador(nombre2, 'Negro', 'Jugando')
        break  # Sale del loop si no hay error
    except NombreVacio as e:
        print(e)  # "No se puede ingresar un nombre vacío"
        # Vuelve a pedir nombres
```

#### `NoSeIngresoEnteroError`

**Cuándo se lanza:**
- Al intentar convertir input de posición a entero
- En `combertir_entero()` si `int(pos)` falla

**Por qué es necesaria:**
- Valida que el usuario ingrese números
- Evita crashes por input inválido
- Idea tomada del proyecto Ta-Te-Ti

**Uso:**
```python
try:
    pos = input("Ingrese la posición inicial: ")
    pos_inic = juego.combertir_entero(pos)  # Puede lanzar excepción
except NoSeIngresoEnteroError as e:
    print(e)  # "Se debe ingresar un numero entero"
    # Vuelve a pedir input
```

**Ejemplo de input inválido:**
```
Usuario ingresa: "abc" → NoSeIngresoEnteroError
Usuario ingresa: "12.5" → NoSeIngresoEnteroError
Usuario ingresa: "12" → ✓ Válido
```

### Estrategia de Manejo de Errores

#### En BackgammonGame

- **Lanza excepciones personalizadas** cuando detecta situaciones especiales
- **No captura sus propias excepciones** (responsabilidad de la UI)
- **Propaga información clara** con mensajes descriptivos

#### En CLI

**Captura todas las excepciones relevantes:**
```python
try:
    # Operaciones del juego
    juego.realizar_movimiento(pos_inic, pos_fin)
except MovimientoInvalido as e:
    print(e)  # Mostrar error y continuar
except NoSeIngresoEnteroError as e:
    print(e)  # Mostrar error y continuar
except NoHayMovimientosPosibles as e:
    print(e)  # Informar y continuar (turno ya cambió)
except Ganador as e:
    print(e)  # Mostrar victoria y salir
    break
```

# Estrategias de testing y covertura

Hay un archivo de test para cada clase del proyecto, donde se testean las funciones de dicha clase y que resultados generará segun el escenario especifico del test, para funciones donde se necesiten valores espeficos de los dados se ha usado mock_randint para que el valor random obtenido al tirar los dados sea un especifico necesario para correcto funcionamiento del test. Para los test del CLI se ha usado mock_input para manejar los inputs del CLI, mock_print para verificar ciertos prints y evitar que la consola se llene de prints y @patch.object(CLI, 'mostrar_tablero') para Evitar renderizar gráficos durante tests (más rápido), Verificar que se llamó al método y Aislar la lógica de negocio de la interfaz.
Se ha buscado que la covertura de los test supere el 90%

# Referencias a requisitos SOLID y como se cumplen

## SRP
 - Board: Solo gestiona el tablero y las fichas
 - MoveValidator: Solo valida movimientos básicos
 - RuleValidator: Solo valida reglas especiales
 - DiceManager: Solo gestiona dados
 - MoveCalculator: Solo calcula movimientos posibles
 - Player: Solo representa jugadores
 - Checker: Solo representa fichas
 - Dice: Solo representa un dado
 - BackGammongame: Orquestar el juego Backgammon

 ## Open/Closed Principle
 - Se puede extender funcionalidad sin modificar clases existentes
 -  Por ejemplo, se prodrían agregar nuevos validadores sin cambiar los existentes

 ## Liskov Substitution Principle
- No hay herencia problemática en tu proyecto
- Las clases son independientes y no hay violaciones

## Interface Segregation Principle
-  Cada clase expone solo los métodos necesarios
- BackgammonGame actúa como fachada coordinando servicios específicos

## Dependency Inversion Principle
- BackgammonGame inyecta dependencias en el constructor

## Anexo: Diagrama de Clases

![Diagrama de Clases](assets/diagrama_de_clases.jpeg)