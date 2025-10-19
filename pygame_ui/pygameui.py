# main_pygame.py
from core.backgammongame import BackgammonGame, MovimientoInvalido, NoHayMovimientosPosibles, Ganador
from pygame_ui.board_adapter import BoardAdapter
import pygame
import sys

WIDTH, HEIGHT = 900, 600
BACKGROUND = (240, 240, 220)
LINE_COLOR = (60, 40, 20)
WHITE = (250, 250, 250)
BLACK = (30, 30, 30)


def main():
    pygame.init()
    pygame.display.set_caption("Backgammon - Mi Juego")
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 20)
    font_big = pygame.font.SysFont(None, 36)

    # TU JUEGO SOLID
    game = BackgammonGame()
    game.inicializar_board()
    game.crear_jugador("Jugador 1", "Blanco", "Jugando")
    game.crear_jugador("Jugador 2", "Negro", "Jugando")
    
    # Adaptador
    board_adapter = BoardAdapter(game)
    
    # Estado UI
    posicion_seleccionada = None
    mensaje = "Presiona ESPACIO para tirar dados"
    hitmap = {}

    running = True
    while running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
            
            elif e.type == pygame.KEYDOWN:
                if e.key in (pygame.K_ESCAPE, pygame.K_q):
                    running = False
                elif e.key == pygame.K_SPACE:
                    # Tirar dados
                    if not game.obtener_dados_disponibles():
                        game.tirar_dados()
                        try:
                            game.verifificar_movimientos_posibles()
                            dados_valores = [d.obtener_numero() for d in game.obtener_dados_disponibles()]
                            mensaje = f"Dados lanzados: {dados_valores}"
                        except NoHayMovimientosPosibles:
                            mensaje = "No hay movimientos. Cambiando turno..."
                            game.cambiar_turno()
                            game.tirar_dados()
                    else:
                        mensaje = "Ya hay dados disponibles"
            
            elif e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                # Primero verificar si clickeó la barra
                bar_click = hit_test_captured(e.pos, game)
                
                if bar_click:
                    # Seleccionó ficha comida
                    if posicion_seleccionada is None:
                        posicion_seleccionada = 'bar'  # Marcador especial
                        mensaje = f"Ficha comida seleccionada. Click en destino (0-5 o 18-23)"
                    else:
                        mensaje = "Ya hay una posición seleccionada"
                else:
                    # Click en tablero normal
                    idx = hit_test(hitmap, e.pos)
                    
                    if idx is not None:
                        if posicion_seleccionada is None:
                            # Verificar si tiene fichas comidas (NO puede mover otras)
                            if game.obtener_board().verificar_ficha_comida(game.obtener_turno()):
                                mensaje = "¡Debes meter primero las fichas comidas!"
                            else:
                                # Seleccionar ficha normal
                                contenedor = game.obtener_board().obtener_contenedor_fichas()
                                if len(contenedor[idx]) > 0:
                                    if contenedor[idx][0].obtener_color() == game.obtener_turno():
                                        posicion_seleccionada = idx
                                        mensaje = f"Seleccionada pos {idx}. Click en destino"
                                    else:
                                        mensaje = f"Pos {idx} no es tu ficha"
                                else:
                                    mensaje = f"Pos {idx} está vacía"
                        
                        elif posicion_seleccionada == 'bar':
                            # Mover desde barra (ficha comida)
                            try:
                                game.realizar_moviento_desde_inicio(idx)
                                mensaje = f"✓ Ficha comida movida a {idx}"
                                posicion_seleccionada = None
                                board_adapter.actualizar()
                            except MovimientoInvalido as ex:
                                mensaje = f"✗ Error: {str(ex)[:50]}"
                                posicion_seleccionada = None
                        
                        else:
                            # Mover ficha normal
                            try:
                                game.realizar_movimiento(posicion_seleccionada, idx)
                                mensaje = f"✓ Movido: {posicion_seleccionada} → {idx}"
                                posicion_seleccionada = None
                                board_adapter.actualizar()
                            except MovimientoInvalido as ex:
                                mensaje = f"✗ Error: {str(ex)[:50]}"
                                posicion_seleccionada = None
                            except Ganador:
                                mensaje = f"🏆 ¡{game.obtener_turno()} GANÓ!"

        # Renderizar
        board_adapter.actualizar()
        hitmap = render_board(screen, board_adapter, font)
        render_captured_pieces(screen, game, font)
        
        # UI INFO (siempre visible)
        turno_text = font_big.render(f"Turno: {game.obtener_turno()}", True, BLACK)
        screen.blit(turno_text, (10, 10))
        
        # DADOS (siempre visible)
        dados = game.obtener_dados_disponibles()
        if dados:
            dados_valores = [d.obtener_numero() for d in dados]
            dados_text = font_big.render(f"Dados: {dados_valores}", True, (0, 100, 0))
        else:
            dados_text = font_big.render("Dados: [] (ESPACIO)", True, (200, 0, 0))
        screen.blit(dados_text, (10, 50))
        
        # MENSAJE
        msg_text = font.render(mensaje, True, BLACK)
        screen.blit(msg_text, (10, HEIGHT - 30))
        
        # Resaltar selección en tablero
        if posicion_seleccionada is not None and posicion_seleccionada != 'bar':
            if posicion_seleccionada in hitmap:
                rect = hitmap[posicion_seleccionada]
                pygame.draw.rect(screen, (255, 215, 0), rect, 3)

        # Resaltar BARRA si está seleccionada
        if posicion_seleccionada == 'bar':
            margin = 40
            barra_x = WIDTH - margin + 10
            turno = game.obtener_turno()
            
            if turno == "Blanco":
                # Resaltar área blanca
                rect = pygame.Rect(barra_x - 25, 120, 50, 180)
            else:
                # Resaltar área negra
                rect = pygame.Rect(barra_x - 25, HEIGHT - 300, 50, 180)
            
            pygame.draw.rect(screen, (255, 215, 0), rect, 3)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()



def render_board(screen, board_adapter, font):
    screen.fill(BACKGROUND)
    board = board_adapter

    margin = 40
    width = WIDTH - 2 * margin
    height = HEIGHT - 2 * margin
    point_width = width // 12
    point_height = height // 2 - 20

    hitmap = {}

    # Dibujar triángulos
    for i in range(12):
        x = margin + i * point_width
        color = (180, 60, 60) if i % 2 == 0 else (240, 200, 80)
        pygame.draw.polygon(screen, color, [
            (x, margin), 
            (x + point_width, margin), 
            (x + point_width//2, margin + point_height)
        ])
        pygame.draw.polygon(screen, color, [
            (x, HEIGHT - margin), 
            (x + point_width, HEIGHT - margin), 
            (x + point_width//2, HEIGHT - margin - point_height)
        ])

    radius = point_width // 3

    # CORRECCIÓN: Crear hitmap para TODAS las posiciones
    for col in range(24):
        data = board.pos.get(col)
        
        # Calcular coordenadas base (SIEMPRE, incluso si está vacío)
        if col < 12:
            i = 11 - col
            base_x = margin + i * point_width + point_width // 2
            rect = pygame.Rect(
                base_x - point_width//2, 
                margin,
                point_width, 
                point_height
            )
        else:
            i = col - 12
            base_x = margin + i * point_width + point_width // 2
            rect = pygame.Rect(
                base_x - point_width//2, 
                HEIGHT - margin - point_height,
                point_width, 
                point_height
            )
        
        # SIEMPRE agregar al hitmap (aunque esté vacío)
        hitmap[col] = rect
        
        # Si no hay fichas, continuar (ya agregamos hitmap)
        if not data:
            continue
        
        # Dibujar fichas si existen
        color_str, count = data
        color = WHITE if color_str == 'white' else BLACK
        text_color = BLACK if color == WHITE else WHITE
        
        if col < 12:
            for n in range(min(count, 4)):
                y = margin + (n * (radius * 2 + 2)) + radius
                pygame.draw.circle(screen, color, (base_x, y), radius)
            
            if count == 5:
                y = margin + (4 * (radius * 2 + 2)) + radius
                pygame.draw.circle(screen, color, (base_x, y), radius)
            elif count > 5:
                accumulated_count = count - 4
                y = margin + (4 * (radius * 2 + 2)) + radius
                pygame.draw.circle(screen, color, (base_x, y), radius)
                text_surface = font.render(str(accumulated_count), True, text_color)
                screen.blit(text_surface, 
                    (base_x - text_surface.get_width() // 2, 
                     y - text_surface.get_height() // 2))
        else:
            for n in range(min(count, 4)):
                y = HEIGHT - margin - (n * (radius * 2 + 2)) - radius
                pygame.draw.circle(screen, color, (base_x, y), radius)
            
            if count == 5:
                y = HEIGHT - margin - (4 * (radius * 2 + 2)) - radius
                pygame.draw.circle(screen, color, (base_x, y), radius)
            elif count > 5:
                accumulated_count = count - 4
                y = HEIGHT - margin - (4 * (radius * 2 + 2)) - radius
                pygame.draw.circle(screen, color, (base_x, y), radius)
                text_surface = font.render(str(accumulated_count), True, text_color)
                screen.blit(text_surface, 
                    (base_x - text_surface.get_width() // 2, 
                     y - text_surface.get_height() // 2))

    return hitmap


def hit_test(hitmap, pos):

    x, y = pos
    for idx, rect in hitmap.items():
        if rect.collidepoint(x, y):
            return idx
    return None

def render_captured_pieces(screen, game, font):
    """
    Renderiza las fichas comidas en la barra lateral derecha.
    """
    margin = 40
    radius = 15
    
    # Obtener fichas comidas
    board = game.obtener_board()
    blancas_comidas = len(board.obtener_contenedor_blancas())
    negras_comidas = len(board.obtener_contenedor_negras())
    
    # Posición de la barra (derecha del tablero)
    barra_x = WIDTH - margin + 10
    
    # Título
    titulo = font.render("Comidas", True, BLACK)
    screen.blit(titulo, (barra_x - 20, 100))
    
    # Fichas BLANCAS comidas (arriba)
    if blancas_comidas > 0:
        y_start = 140
        for i in range(min(blancas_comidas, 5)):
            y = y_start + (i * (radius * 2 + 4))
            pygame.draw.circle(screen, WHITE, (barra_x, y), radius)
            pygame.draw.circle(screen, BLACK, (barra_x, y), radius, 2)  # Borde
        
        # Si hay más de 5, mostrar número
        if blancas_comidas > 5:
            y = y_start + (4 * (radius * 2 + 4))
            pygame.draw.circle(screen, WHITE, (barra_x, y), radius)
            text_surface = font.render(str(blancas_comidas - 4), True, BLACK)
            screen.blit(text_surface, 
                (barra_x - text_surface.get_width() // 2, 
                 y - text_surface.get_height() // 2))
    
    # Fichas NEGRAS comidas (abajo)
    if negras_comidas > 0:
        y_start = HEIGHT - 140
        for i in range(min(negras_comidas, 5)):
            y = y_start - (i * (radius * 2 + 4))
            pygame.draw.circle(screen, BLACK, (barra_x, y), radius)
            pygame.draw.circle(screen, WHITE, (barra_x, y), radius, 2)  # Borde
        
        # Si hay más de 5, mostrar número
        if negras_comidas > 5:
            y = y_start - (4 * (radius * 2 + 4))
            pygame.draw.circle(screen, BLACK, (barra_x, y), radius)
            text_surface = font.render(str(negras_comidas - 4), True, WHITE)
            screen.blit(text_surface, 
                (barra_x - text_surface.get_width() // 2, 
                 y - text_surface.get_height() // 2))

def hit_test_captured(pos, game):
    """
    Detecta si el click es en la zona de fichas comidas.
    Retorna 'bar_white' o 'bar_black' si hay ficha comida del turno actual.
    """
    margin = 40
    barra_x = WIDTH - margin + 10
    radius = 15
    
    x, y = pos
    
    # Verificar si está cerca de la barra (área clickeable)
    if not (barra_x - 30 <= x <= barra_x + 30):
        return None
    
    turno = game.obtener_turno()
    board = game.obtener_board()
    
    # Verificar fichas BLANCAS comidas
    if turno == "Blanco" and len(board.obtener_contenedor_blancas()) > 0:
        # Área de fichas blancas (arriba)
        if 120 <= y <= 300:
            return 'bar_white'
    
    # Verificar fichas NEGRAS comidas
    if turno == "Negro" and len(board.obtener_contenedor_negras()) > 0:
        # Área de fichas negras (abajo)
        if HEIGHT - 300 <= y <= HEIGHT - 120:
            return 'bar_black'
    
    return None


if __name__ == "__main__":
    main()