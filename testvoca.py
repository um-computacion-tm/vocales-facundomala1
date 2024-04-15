import unittest
from voca import contador_vocales

class TestVoca(unittest.TestCase):
    def test_sin_vocales(self):

        palabra = "tryhgf"

        resultado = contador_vocales(palabra)

        self.assertEqual(resultado, {})



    def test_con_vocal_o(self):

        palabra = "mall"

        resultado = contador_vocales(palabra)

        self.assertEqual(resultado, {"a": 1})



    def test_con_vocal_doble_o(self):

        palabra = "oso"

        resultado = contador_vocales(palabra)

        self.assertEqual(resultado, {"o": 2})



    def test_con_dos_vocales(self):

        palabra = "ceja"

        resultado = contador_vocales(palabra)

        self.assertEqual(resultado, {"e": 1, "a": 1})



    def test_con_todas_las_vocales(self):

        palabra = "solamente quiero que gane river"

        resultado = contador_vocales(palabra)

        self.assertEqual(

            resultado,

            {"a": 2, "e": 6, "i": 2, "o": 2, "u": 2},

        )



    def test_con_vocales_en_mayuscula(self):

        palabra = "sOy faN de pyThOn Desde hoy"

        resultado = contador_vocales(palabra)

        self.assertEqual(

            resultado,

            {"a": 1, "e": 3, "o": 3,},

        )

unittest.main()