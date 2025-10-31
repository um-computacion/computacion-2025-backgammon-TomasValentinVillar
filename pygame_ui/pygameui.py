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
    estado = "JUGANDO"  # Puede ser: "JUGANDO" o "GANADOR"
    ganador = None

    running = True
    while running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
            
            elif e.type == pygame.KEYDOWN:
                if e.key in (pygame.K_ESCAPE, pygame.K_q):
                    running = False
                
                elif e.key == pygame.K_r and estado == "GANADOR":
                    # ✅ Reiniciar juego
                    game = BackgammonGame()
                    game.inicializar_board()
                    game.crear_jugador("Jugador 1", "Blanco", "Jugando")
                    game.crear_jugador("Jugador 2", "Negro", "Jugando")
                    board_adapter = BoardAdapter(game)
                    estado = "JUGANDO"
                    posicion_seleccionada = None
                    mensaje = "Presiona ESPACIO para tirar dados"
                
                elif e.key == pygame.K_SPACE:
                    # ✅ Solo permitir tirar dados si NO hay ganador
                    if estado == "GANADOR":
                        mensaje = "¡Juego terminado! Presiona R para reiniciar o ESC para salir"
                    elif not game.obtener_dados_disponibles():
                        game.tirar_dados()
                        try:
                            game.verifificar_movimientos_posibles()
                            dados_valores = [d.obtener_numero() for d in game.obtener_dados_disponibles()]
                            mensaje = f"Dados lanzados: {dados_valores}"
                        except NoHayMovimientosPosibles:
                            mensaje = "No hay movimientos. Cambiando turno..."
                    else:
                        mensaje = "Ya hay dados disponibles"
            
            elif e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                # ✅ Solo permitir clicks si NO hay ganador
                if estado == "GANADOR":
                    continue  # Ignorar clicks
                
                # NUEVO: Verificar bear off primero
                bear_off_pos = hit_test_bear_off(e.pos, game)
                
                if bear_off_pos is not None:
                    # ═══════════════════════════════════════
                    # CASO: Click en zona de SACAR fichas
                    # ═══════════════════════════════════════
                    if posicion_seleccionada is not None and posicion_seleccionada != 'bar':
                        # Intentar sacar ficha
                        try:
                            game.realizar_movimiento(posicion_seleccionada, bear_off_pos)
                            mensaje = f"✓ Ficha sacada desde {posicion_seleccionada}"
                            posicion_seleccionada = None
                            board_adapter.actualizar()
                        except MovimientoInvalido as ex:
                            mensaje = f"✗ No puedes sacar: {str(ex)[:40]}"
                            posicion_seleccionada = None
                        except Ganador:
                            # ✅ AGREGADO: Manejar victoria al sacar ficha
                            estado = "GANADOR"
                            ganador = game.obtener_turno()
                            mensaje = f"🏆 ¡{ganador} GANÓ LA PARTIDA!"
                            posicion_seleccionada = None
                            board_adapter.actualizar()
                    else:
                        mensaje = "Selecciona primero una ficha para sacar"
                
                else:
                    # Verificar barra (fichas comidas)
                    bar_click = hit_test_captured(e.pos, game)
                    
                    if bar_click:
                        # Seleccionó ficha comida
                        if posicion_seleccionada is None:
                            posicion_seleccionada = 'bar'
                            mensaje = f"Ficha comida seleccionada. Click en destino"
                        else:
                            mensaje = "Ya hay una posición seleccionada"
                    
                    else:
                        # Verificar tablero normal
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
                                    estado = "GANADOR"
                                    ganador = game.obtener_turno()
                                    mensaje = f"🏆 ¡{ganador} GANÓ LA PARTIDA!"
                                    posicion_seleccionada = None
                                    board_adapter.actualizar()

        # Renderizar
        board_adapter.actualizar()
        hitmap = render_board(screen, board_adapter, font)
        render_captured_pieces(screen, game, font)
        render_bear_off_zones(screen, game, font)

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
                rect = pygame.Rect(barra_x - 25, 120, 50, 180)
            else:
                rect = pygame.Rect(barra_x - 25, HEIGHT - 300, 50, 180)
            
            pygame.draw.rect(screen, (255, 215, 0), rect, 3)
        
        # ═══════════════════════════════════════════════════════════
        # ✅ PANTALLA DE VICTORIA (OVERLAY)
        # ═══════════════════════════════════════════════════════════
        if estado == "GANADOR":
            # Overlay oscuro
            overlay = pygame.Surface((WIDTH, HEIGHT))
            overlay.set_alpha(180)
            overlay.fill((0, 0, 0))
            screen.blit(overlay, (0, 0))
            
            # Mensaje principal
            victoria_text = pygame.font.SysFont(None, 72).render(
                f"🏆 {ganador} GANÓ! 🏆", 
                True, 
                (255, 215, 0)
            )
            text_rect = victoria_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
            screen.blit(victoria_text, text_rect)
            
            # Submensaje
            sub_text = font_big.render(
                "Presiona ESC para salir o R para reiniciar", 
                True, 
                WHITE
            )
            sub_rect = sub_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
            screen.blit(sub_text, sub_rect)

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

    # Crear hitmap para TODAS las posiciones
    for col in range(24):
        data = board.__pos__.get(col)
        
        # Calcular coordenadas base (SIEMPRE)
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
        
        # SIEMPRE agregar al hitmap
        hitmap[col] = rect
        
        if not data:
            continue
        
        # Dibujar fichas
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
    
    board = game.obtener_board()
    blancas_comidas = len(board.obtener_contenedor_blancas())
    negras_comidas = len(board.obtener_contenedor_negras())
    
    barra_x = WIDTH - margin + 10
    
    titulo = font.render("Comidas", True, BLACK)
    screen.blit(titulo, (barra_x - 20, 100))
    
    # Fichas BLANCAS comidas (arriba)
    if blancas_comidas > 0:
        y_start = 140
        for i in range(min(blancas_comidas, 5)):
            y = y_start + (i * (radius * 2 + 4))
            pygame.draw.circle(screen, WHITE, (barra_x, y), radius)
            pygame.draw.circle(screen, BLACK, (barra_x, y), radius, 2)
        
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
            pygame.draw.circle(screen, WHITE, (barra_x, y), radius, 2)
        
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
    """
    margin = 40
    barra_x = WIDTH - margin + 10
    
    x, y = pos
    
    if not (barra_x - 30 <= x <= barra_x + 30):
        return None
    
    turno = game.obtener_turno()
    board = game.obtener_board()
    
    if turno == "Blanco" and len(board.obtener_contenedor_blancas()) > 0:
        if 120 <= y <= 300:
            return 'bar_white'
    
    if turno == "Negro" and len(board.obtener_contenedor_negras()) > 0:
        if HEIGHT - 300 <= y <= HEIGHT - 120:
            return 'bar_black'
    
    return None


def render_bear_off_zones(screen, game, font):
    """
    """
    margin = 40
    font_small = pygame.font.SysFont(None, 16)
    
    board = game.obtener_board()
    blancas_sacadas = len(board.obtener_contenedor_blancas_sacadas())
    negras_sacadas = len(board.obtener_contenedor_negras_sacadas())
    
    # ═══════════════════════════════════════
    # ZONA BLANCAS (extremo derecho absoluto)
    # ═══════════════════════════════════════
    zona_blancas = pygame.Rect(
        WIDTH - 30,              # ✅ Pegado al borde derecho
        HEIGHT // 2 + 60,
        25,                      # ✅ MUY estrecha
        HEIGHT // 2 - margin - 80
    )
    
    pygame.draw.rect(screen, (200, 220, 200), zona_blancas)
    pygame.draw.rect(screen, BLACK, zona_blancas, 2)
    
    # Título vertical
    titulo_b = font_small.render("OUT", True, BLACK)
    titulo_rotado = pygame.transform.rotate(titulo_b, 90)
    screen.blit(titulo_rotado, (zona_blancas.centerx - 8, zona_blancas.y + 10))
    
    if blancas_sacadas > 0:
        radius = 7
        y_start = zona_blancas.y + 50
        
        for i in range(min(blancas_sacadas, 3)):
            y = y_start + (i * (radius * 2 + 2))
            pygame.draw.circle(screen, WHITE, (zona_blancas.centerx, y), radius)
            pygame.draw.circle(screen, BLACK, (zona_blancas.centerx, y), radius, 1)
        
        if blancas_sacadas > 3:
            y = y_start + (2 * (radius * 2 + 2))
            pygame.draw.circle(screen, WHITE, (zona_blancas.centerx, y), radius)
            text_surface = font_small.render(str(blancas_sacadas - 2), True, BLACK)
            screen.blit(text_surface, 
                (zona_blancas.centerx - text_surface.get_width() // 2, 
                 y - text_surface.get_height() // 2))
        
        total_text = font_small.render(f"{blancas_sacadas}/15", True, BLACK)
        screen.blit(total_text, 
            (zona_blancas.centerx - total_text.get_width() // 2, 
             zona_blancas.bottom - 15))
    
    # ═══════════════════════════════════════
    # ZONA NEGRAS (extremo izquierdo absoluto)
    # ═══════════════════════════════════════
    zona_negras = pygame.Rect(
        5,                       # ✅ Pegado al borde izquierdo
        margin + 40,
        25,                      # ✅ MUY estrecha
        HEIGHT // 2 - margin - 80
    )
    
    pygame.draw.rect(screen, (200, 220, 200), zona_negras)
    pygame.draw.rect(screen, BLACK, zona_negras, 2)
    
    titulo_n = font_small.render("OUT", True, BLACK)
    titulo_rotado_n = pygame.transform.rotate(titulo_n, 90)
    screen.blit(titulo_rotado_n, (zona_negras.centerx - 8, zona_negras.y + 10))
    
    if negras_sacadas > 0:
        radius = 7
        y_start = zona_negras.y + 50
        
        for i in range(min(negras_sacadas, 3)):
            y = y_start + (i * (radius * 2 + 2))
            pygame.draw.circle(screen, BLACK, (zona_negras.centerx, y), radius)
            pygame.draw.circle(screen, WHITE, (zona_negras.centerx, y), radius, 1)
        
        if negras_sacadas > 3:
            y = y_start + (2 * (radius * 2 + 2))
            pygame.draw.circle(screen, BLACK, (zona_negras.centerx, y), radius)
            text_surface = font_small.render(str(negras_sacadas - 2), True, WHITE)
            screen.blit(text_surface, 
                (zona_negras.centerx - text_surface.get_width() // 2, 
                 y - text_surface.get_height() // 2))
        
        total_text = font_small.render(f"{negras_sacadas}/15", True, BLACK)
        screen.blit(total_text, 
            (zona_negras.centerx - total_text.get_width() // 2, 
             zona_negras.bottom - 15))
    
    # Resaltar si puede sacar
    turno = game.obtener_turno()
    if turno == "Blanco":
        if puede_empezar_bear_off(game, "Blanco"):
            pygame.draw.rect(screen, (100, 255, 100), zona_blancas, 3)
    else:
        if puede_empezar_bear_off(game, "Negro"):
            pygame.draw.rect(screen, (100, 255, 100), zona_negras, 3)


def hit_test_bear_off(pos, game):
    """
    ✅ CORREGIDO: Coordenadas ajustadas a zonas pegadas a bordes
    """
    x, y = pos
    margin = 40
    
    turno = game.obtener_turno()
    
    # Zona BLANCAS (extremo derecho)
    if turno == "Blanco":
        zona_x_start = WIDTH - 30
        zona_x_end = WIDTH - 5
        zona_y_start = HEIGHT // 2 + 60
        zona_y_end = HEIGHT - margin - 20
        
        if zona_x_start <= x <= zona_x_end:
            if zona_y_start <= y <= zona_y_end:
                if game.obtener_board().verficar_fichas_sacadas_15(turno):
                    return None
                return 24
    
    # Zona NEGRAS (extremo izquierdo)
    if turno == "Negro":
        zona_x_start = 5
        zona_x_end = 30
        zona_y_start = margin + 40
        zona_y_end = HEIGHT // 2 - 40
        
        if zona_x_start <= x <= zona_x_end:
            if zona_y_start <= y <= zona_y_end:
                if game.obtener_board().verficar_fichas_sacadas_15(turno):
                    return None
                return -1
    
    return None


def puede_empezar_bear_off(game, turno):
    """
    Verifica si todas las fichas están en home board.
    """
    contenedor = game.obtener_board().obtener_contenedor_fichas()
    
    if turno == "Blanco":
        for pos in range(18):
            if len(contenedor[pos]) > 0:
                if contenedor[pos][0].obtener_color() == "Blanco":
                    return False
        return True
    else:
        for pos in range(6, 24):
            if len(contenedor[pos]) > 0:
                if contenedor[pos][0].obtener_color() == "Negro":
                    return False
        return True


if __name__ == "__main__":
    main()