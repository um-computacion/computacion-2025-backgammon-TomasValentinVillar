'''
Modulo encargado de la linea de comando
contiene a la clase CLI
'''

from core.backgammongame import BackgammonGame, NoHayMovimientosPosibles,MovimientoInvalido, Ganador, NombreVacio, NoSeIngresoEnteroError
class CLI:
    '''
    Clase encargada de la linea de comando para ejectar el Proyecto
    '''

    def __init__(self):
        self.__juego__ = BackgammonGame()

    def mostrar_tablero(self):
        '''
        Represtentación grafica del tablero de Backgammon, utiliza la la funcion draw_full_board 
        para obtener las filaes del tablero y hacer los print
        '''
        board_draw= self.__juego__.obtener_board().draw_full_board()
        print("   Pos: 11 10  9  8  7  6   5  4  3  2  1  0")
        print("-" * 50)

        for row in range(5):
            row_str = "        "
            for col in range(12):
                row_str += f" {board_draw[row][col]} "
                if col == 5:
                    row_str += '|'
            print(row_str)

        print("\n" + "-"*50)

        # Mostrar segunda mitad (posiciones 12-23)
        print("   Pos: 12 13 14 15 16 17   18 19 20 21 22 23")
        print("-" * 50)
        for row in range(5,10):
            row_str = "        "
            for col in range(12):
                row_str += f" {board_draw[row][col]} "
                if col == 5:
                    row_str += '|'
            print(row_str)

    def ejecutar(self):
        self.__juego__.inicializar_board()
        while True:
            try:
                nombre1 = input('Ingrese el nombre del jugador para las fichas Blancas: ')
                nombre2 = input('Ingrese el nombre del jugador para las fichas Negras: ')
                self.__juego__.crear_jugador(nombre1,'Blanco','Jugando')
                self.__juego__.crear_jugador(nombre2,'Negro','Juagando')
                break
            except NombreVacio as e:
                print(e)

        while True:

            print("Tablero")
            if len(self.__juego__.obtener_dados_disponibles()) == 0:
                self.__juego__.tirar_dados()
            try:
                while True:
                    if self.__juego__.obtener_board().verificar_ficha_comida(self.__juego__.obtener_turno()):
                        self.mostrar_tablero()
                        print(f'Truno: {self.__juego__.obtener_players()[self.__juego__.obtener_turno()].obtener_nombre()}, Ficha: {self.__juego__.obtener_turno()}')
                        lista_dados = ''
                        for i in self.__juego__.obtener_dados_disponibles():
                            lista_dados += f'{str(i.obtener_numero())}, '
                        print(f"Sus dados disponibles son: {lista_dados}")
                        print(f"Tienes {self.__juego__.obtener_board().obtener_cantidad_de_fichas_comidas(self.__juego__.obtener_turno())} fichas que se han comido ")
                        self.__juego__.verifificar_movimientos_posibles()
                        pos_fin = input("Ingrese la pocición final: ")
                        pos_fin = int(pos_fin)
                        self.__juego__.realizar_moviento_desde_inicio(pos_fin)
                        if len(self.__juego__.obtener_dados_disponibles()) == 0:
                            break
                        print("-" * 50)
                    else:
                        print(f'Truno: {self.__juego__.obtener_players()[self.__juego__.obtener_turno()].obtener_nombre()}, Ficha: {self.__juego__.obtener_turno()}')
                        self.mostrar_tablero()
                        lista_dados = ''
                        for i in self.__juego__.obtener_dados_disponibles():
                            lista_dados += f'{str(i.obtener_numero())}, '
                        print(f"Sus dados disponibles son: {lista_dados}")
                        self.__juego__.verifificar_movimientos_posibles()
                        pos = input("Ingrese la pocición inicial: ")
                        pos_inic = self.__juego__.combertir_entero(pos)
                        pos = input("Ingrese la pocición final: ")
                        pos_fin = self.__juego__.combertir_entero(pos)
                        self.__juego__.realizar_movimiento(pos_inic,pos_fin)
                        if len(self.__juego__.obtener_dados_disponibles()) == 0:
                            break
                        print("-" * 50)

            except MovimientoInvalido as e:
                print(e)
            
            except NoSeIngresoEnteroError as e:
                print(e)

            except NoHayMovimientosPosibles as e:
                self.__juego__.cambiar_turno()
                print(e)

            except Ganador as e:
                self.mostrar_tablero()
                print(e)
                break

if __name__ == '__main__':
    cli = CLI()
    cli.ejecutar()
