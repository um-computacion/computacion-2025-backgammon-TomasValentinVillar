"""
Interfaz gráfica principal del juego Backgammon usando Pygame.
Maneja la ventana, eventos y renderizado del juego.
"""
import pygame
import sys
from core.backgammongame import BackgammonGame, MovimientoInvalido, NoHayMovimientosPosibles, Ganador
from pygame_ui.colors import *


class BackgammonUI:
    """
    Interfaz gráfica del juego Backgammon.
    Responsabilidad: Manejar la visualización y entrada del usuario (SRP).
    """
    
    def __init__(self, ancho=1200, alto=800):
        """
        Inicializa Pygame y la ventana del juego.
        
        Args:
            ancho: Ancho de la ventana en píxeles
            alto: Alto de la ventana en píxeles
        """
        # Inicializar Pygame
        pygame.init()
        pygame.font.init()
        
        # Configuración de ventana
        self.ancho = ancho
        self.alto = alto
        self.pantalla = pygame.display.set_mode((ancho, alto))
        pygame.display.set_caption("Backgammon - Juego de Estrategia")
        
        # Reloj para controlar FPS
        self.reloj = pygame.time.Clock()
        self.fps = 60
        
        # Fuentes
        self.fuente_grande = pygame.font.Font(None, 48)
        self.fuente_mediana = pygame.font.Font(None, 36)
        self.fuente_pequeña = pygame.font.Font(None, 24)
        
        # Estado del juego
        self.juego = BackgammonGame()
        self.jugando = True
        self.estado = "MENU"  # Estados: MENU, JUGANDO, GANADOR
        
        # Estado de interacción
        self.posicion_seleccionada = None
        self.posiciones_validas = []
        
        # Dimensiones del tablero
        self.calcular_dimensiones()
    
    def calcular_dimensiones(self):
        """
        Calcula las dimensiones y posiciones de los elementos del tablero.
        """
        # Área del tablero (80% del ancho, centrado)
        self.tablero_ancho = int(self.ancho * 0.8)
        self.tablero_alto = int(self.alto * 0.7)
        self.tablero_x = (self.ancho - self.tablero_ancho) // 2
        self.tablero_y = 100
        
        # Dimensiones de puntos (triángulos)
        self.punto_ancho = self.tablero_ancho // 14  # 12 puntos + 2 espacios
        self.punto_alto = self.tablero_alto // 2 - 20
        
        # Tamaño de fichas
        self.ficha_radio = min(self.punto_ancho // 2 - 5, 25)
        
        # Área de información (arriba)
        self.info_alto = 80
        
        # Área de dados (derecha)
        self.dados_x = self.tablero_x + self.tablero_ancho + 20
        self.dados_y = self.tablero_y + 100
        self.dado_tamaño = 60
    
    def ejecutar(self):
        """
        Loop principal del juego.
        """
        while self.jugando:
            self.manejar_eventos()
            self.actualizar()
            self.renderizar()
            self.reloj.tick(self.fps)
        
        pygame.quit()
        sys.exit()
    
    def manejar_eventos(self):
        """
        Procesa los eventos de Pygame (clicks, teclas, etc.).
        """
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                self.jugando = False
            
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    if self.estado == "JUGANDO":
                        self.estado = "MENU"
                    else:
                        self.jugando = False
            
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if evento.button == 1:  # Click izquierdo
                    self.manejar_click(evento.pos)
    
    def manejar_click(self, pos):
        """
        Maneja los clicks del mouse según el estado del juego.
        
        Args:
            pos: Tupla (x, y) con la posición del click
        """
        if self.estado == "MENU":
            self.manejar_click_menu(pos)
        elif self.estado == "JUGANDO":
            self.manejar_click_tablero(pos)
        elif self.estado == "GANADOR":
            self.manejar_click_ganador(pos)
    
    def manejar_click_menu(self, pos):
        """
        Maneja clicks en el menú principal.
        """
        # Botón "Jugar"
        boton_jugar = pygame.Rect(self.ancho // 2 - 100, self.alto // 2 - 30, 200, 60)
        if boton_jugar.collidepoint(pos):
            self.iniciar_juego()
    
    def manejar_click_tablero(self, pos):
        """
        Maneja clicks en el tablero durante el juego.
        Implementa la lógica de selección y movimiento.
        """
        # Verificar si clickeó en el botón de tirar dados
        boton_dados = self.obtener_rect_boton_dados()
        if boton_dados.collidepoint(pos):
            self.tirar_dados()
            return
        
        # Obtener posición del tablero clickeada
        posicion = self.obtener_posicion_desde_click(pos)
        
        if posicion is not None:
            if self.posicion_seleccionada is None:
                # Primera selección: seleccionar ficha
                self.seleccionar_posicion(posicion)
            else:
                # Segunda selección: mover ficha
                self.mover_ficha(self.posicion_seleccionada, posicion)
    
    def manejar_click_ganador(self, pos):
        """
        Maneja clicks en la pantalla de ganador.
        """
        # Botón "Volver al menú"
        boton_menu = pygame.Rect(self.ancho // 2 - 100, self.alto // 2 + 50, 200, 60)
        if boton_menu.collidepoint(pos):
            self.estado = "MENU"
    
    def iniciar_juego(self):
        """
        Inicia una nueva partida.
        """
        self.juego = BackgammonGame()
        self.juego.inicializar_board()
        self.juego.crear_jugador("Jugador 1", "Blanco", "Jugando")
        self.juego.crear_jugador("Jugador 2", "Negro", "Jugando")
        self.estado = "JUGANDO"
        self.posicion_seleccionada = None
        self.posiciones_validas = []
    
    def tirar_dados(self):
        """
        Tira los dados si no hay dados disponibles.
        """
        if not self.juego.obtener_dados_disponibles():
            self.juego.tirar_dados()
            # Verificar si hay movimientos posibles
            try:
                self.juego.verifificar_movimientos_posibles()
            except NoHayMovimientosPosibles:
                # No hay movimientos, cambiar turno automáticamente
                print("No hay movimientos posibles. Cambiando turno...")
                self.juego.cambiar_turno()
                self.juego.tirar_dados()
    
    def seleccionar_posicion(self, posicion):
        """
        Selecciona una posición del tablero.
        Verifica que haya una ficha del turno actual.
        """
        board = self.juego.obtener_board()
        contenedor = board.obtener_contenedor_fichas()
        turno = self.juego.obtener_turno()
        
        # Verificar que hay ficha y es del turno actual
        if len(contenedor[posicion]) > 0:
            if contenedor[posicion][0].obtener_color() == turno:
                self.posicion_seleccionada = posicion
                # TODO: Calcular posiciones válidas
                print(f"Seleccionada posición {posicion}")
    
    def mover_ficha(self, origen, destino):
        """
        Intenta mover una ficha de origen a destino.
        """
        try:
            self.juego.realizar_movimiento(origen, destino)
            print(f"Movimiento exitoso: {origen} -> {destino}")
            self.posicion_seleccionada = None
        except MovimientoInvalido as e:
            print(f"Movimiento inválido: {e}")
            self.posicion_seleccionada = None
        except Ganador:
            print("¡Hay un ganador!")
            self.estado = "GANADOR"
    
    def obtener_posicion_desde_click(self, pos):
        """
        Convierte una posición de click (x, y) en una posición del tablero (0-23).
        
        Returns:
            int o None: Posición del tablero o None si el click está fuera
        """
        x, y = pos
        
        # Verificar que está dentro del área del tablero
        if not (self.tablero_x <= x <= self.tablero_x + self.tablero_ancho):
            return None
        if not (self.tablero_y <= y <= self.tablero_y + self.tablero_alto):
            return None
        
        # TODO: Implementar conversión precisa de coordenadas a posición
        # Por ahora retorna None
        return None
    
    def obtener_rect_boton_dados(self):
        """
        Retorna el rectángulo del botón de tirar dados.
        """
        return pygame.Rect(self.dados_x, self.dados_y + 200, 150, 50)
    
    def actualizar(self):
        """
        Actualiza la lógica del juego cada frame.
        """
        # Por ahora no hay lógica que actualizar cada frame
        pass
    
    def renderizar(self):
        """
        Dibuja todo en la pantalla.
        """
        # Limpiar pantalla
        self.pantalla.fill(TABLERO_FONDO)
        
        if self.estado == "MENU":
            self.renderizar_menu()
        elif self.estado == "JUGANDO":
            self.renderizar_juego()
        elif self.estado == "GANADOR":
            self.renderizar_ganador()
        
        # Actualizar pantalla
        pygame.display.flip()
    
    def renderizar_menu(self):
        """
        Renderiza el menú principal.
        """
        # Título
        titulo = self.fuente_grande.render("BACKGAMMON", True, BLANCO)
        titulo_rect = titulo.get_rect(center=(self.ancho // 2, self.alto // 3))
        self.pantalla.blit(titulo, titulo_rect)
        
        # Botón Jugar
        boton_rect = pygame.Rect(self.ancho // 2 - 100, self.alto // 2 - 30, 200, 60)
        pygame.draw.rect(self.pantalla, BOTON_NORMAL, boton_rect, border_radius=10)
        pygame.draw.rect(self.pantalla, BLANCO, boton_rect, 3, border_radius=10)
        
        texto = self.fuente_mediana.render("JUGAR", True, TEXTO_BOTON)
        texto_rect = texto.get_rect(center=boton_rect.center)
        self.pantalla.blit(texto, texto_rect)
    
    def renderizar_juego(self):
        """
        Renderiza el estado del juego.
        """
        # Renderizar información del turno
        self.renderizar_info()
        
        # Renderizar tablero (por ahora un rectángulo)
        tablero_rect = pygame.Rect(
            self.tablero_x, self.tablero_y,
            self.tablero_ancho, self.tablero_alto
        )
        pygame.draw.rect(self.pantalla, TABLERO_BORDE, tablero_rect)
        pygame.draw.rect(self.pantalla, PUNTO_CLARO, tablero_rect.inflate(-10, -10))
        
        # TODO: Renderizar puntos (triángulos)
        # TODO: Renderizar fichas
        
        # Renderizar dados
        self.renderizar_dados()
        
        # Renderizar botón de tirar dados
        self.renderizar_boton_dados()
    
    def renderizar_info(self):
        """
        Renderiza la información del turno actual.
        """
        turno = self.juego.obtener_turno()
        texto = self.fuente_mediana.render(
            f"Turno: {turno}",
            True,
            JUGADOR_ACTIVO
        )
        self.pantalla.blit(texto, (50, 30))
    
    def renderizar_dados(self):
        """
        Renderiza los dados disponibles.
        """
        dados = self.juego.obtener_dados_disponibles()
        
        for i, dado in enumerate(dados):
            x = self.dados_x + (i % 2) * 70
            y = self.dados_y + (i // 2) * 70
            self.dibujar_dado(x, y, dado.obtener_numero())
    
    def dibujar_dado(self, x, y, valor):
        """
        Dibuja un dado con su valor.
        """
        # Fondo del dado
        dado_rect = pygame.Rect(x, y, self.dado_tamaño, self.dado_tamaño)
        pygame.draw.rect(self.pantalla, DADO_FONDO, dado_rect, border_radius=8)
        pygame.draw.rect(self.pantalla, DADO_BORDE, dado_rect, 3, border_radius=8)
        
        # Número del dado
        texto = self.fuente_grande.render(str(valor), True, DADO_PUNTO)
        texto_rect = texto.get_rect(center=dado_rect.center)
        self.pantalla.blit(texto, texto_rect)
    
    def renderizar_boton_dados(self):
        """
        Renderiza el botón para tirar dados.
        """
        if not self.juego.obtener_dados_disponibles():
            boton_rect = self.obtener_rect_boton_dados()
            pygame.draw.rect(self.pantalla, BOTON_NORMAL, boton_rect, border_radius=8)
            
            texto = self.fuente_pequeña.render("TIRAR DADOS", True, TEXTO_BOTON)
            texto_rect = texto.get_rect(center=boton_rect.center)
            self.pantalla.blit(texto, texto_rect)
    
    def renderizar_ganador(self):
        """
        Renderiza la pantalla de ganador.
        """
        # Fondo semi-transparente
        overlay = pygame.Surface((self.ancho, self.alto))
        overlay.set_alpha(200)
        overlay.fill(NEGRO)
        self.pantalla.blit(overlay, (0, 0))
        
        # Mensaje de ganador
        ganador = self.juego.obtener_turno()
        texto = self.fuente_grande.render(
            f"¡{ganador} GANÓ!",
            True,
            SELECCIONADO
        )
        texto_rect = texto.get_rect(center=(self.ancho // 2, self.alto // 2 - 50))
        self.pantalla.blit(texto, texto_rect)
        
        # Botón volver al menú
        boton_rect = pygame.Rect(self.ancho // 2 - 100, self.alto // 2 + 50, 200, 60)
        pygame.draw.rect(self.pantalla, BOTON_NORMAL, boton_rect, border_radius=10)
        
        texto = self.fuente_mediana.render("MENÚ", True, TEXTO_BOTON)
        texto_rect = texto.get_rect(center=boton_rect.center)
        self.pantalla.blit(texto, texto_rect)