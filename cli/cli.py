from core.backgammongame import BackgammonGame
class CLI:

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
            row_str = f"        "
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
            row_str = f"        "
            for col in range(12):
                row_str += f" {board_draw[row][col]} "
                if col == 5:
                    row_str += '|'
            print(row_str)
    
    def ejecutar(self):
        self.__juego__.inicializar_board()
        while True:   
            nombre1 = input('Ingrese el nombre del jugador para las fichas Blancas: ')
            nombre2 = input('Ingrese el nombre del jugador para las fichas Negras: ')
            self.__juego__.crear_jugador(nombre1,'Blanco','Jugando')
            self.__juego__.crear_jugador(nombre2,'Negro','Juagando')
            break
        
        while True:
            print("Tablero")
            self.mostrar_tablero()
            print(f'Truno: {self.__juego__.obtener_players()[self.__juego__.obtener_turno()].obtener_nombre()}, Ficha: {self.__juego__.obtener_turno()}')
            try:
                if self.__juego__ == "Blanco":
                    if len(self.__juego__.obtener_board().obtener_contenedor_blancas()) > 0:
                        self.__juego__.



if __name__ == '__main__':
    cli = CLI()
    cli.ejecutar()
