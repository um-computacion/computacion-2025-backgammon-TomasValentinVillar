from core.models.checker import Checker
import unittest

class TestChecker(unittest.TestCase):
    def test_obtener_color_blanco(self):
        ficha = Checker("Blanco")
        self.assertEqual(ficha.obtener_color(),"Blanco")

    def test_obtener_colo_negro(self):
        ficha = Checker("Negro")
        self.assertEqual(ficha.obtener_color(),"Negro")