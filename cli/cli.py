from core.backgammongame import BackgammonGame
class CLI:

    def __init__(self):
        self.__juego__ = BackgammonGame()
    
    def mostrar_tablero(self):
        '''
        Represtentación grafica del tablero de Backgammon, utiliza la la funcion draw_full_board 
        para obtener las filaes del tablero y hacer los print
        '''
        self.__juego__.inicializar_board()
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

if __name__ == '__main__':
    cli = CLI()
    cli.ejecutar()
