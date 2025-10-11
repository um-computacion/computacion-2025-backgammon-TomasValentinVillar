from core.models.player import Player
import unittest

class TestPlayer(unittest.TestCase):
    def test_obtener_nombre(self):
        player = Player("Tomas","Blanco","Jugando")
        self.assertEqual(player.obtener_nombre(),"Tomas")
    
    def test_obtener_ficha(self):
        player = Player("Tomas","Blanco","Jugando")
        self.assertEqual(player.obtener_ficha(),"Blanco")
    
    def test_obtener_estado(self):
        player = Player("Tomas","Blanco","Jugando")
        self.assertEqual(player.obtener_estado(),"Jugando")
    
    def test_definir_ganador(self):
        player = Player("Tomas","Blanco","Jugando")
        player.definir_ganador()
        self.assertEqual(player.obtener_estado(),"Ganador")
    
    def test_definir_perdedor(self):
        player = Player("Tomas","Blanco","Jugando")
        player.definir_perdedor()
        self.assertEqual(player.obtener_estado(),"Perdedor")
