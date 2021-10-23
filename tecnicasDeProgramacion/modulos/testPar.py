#Para testear los diferentes módulos debemos importar unittest y el módulo a testear


import unittest
import ejemploFuncion

#Creamos la clase que testeará el módulo
class TestPar(unittest.TestCase):
    #creamos el método que va a analizar los ejercicios
    def test_par(self):
        self.assertEqual(ejemploFuncion.esPar(2), "Par")
        self.assertEqual(ejemploFuncion.esPar(3),"Impar")

if __name__ == "__main__":
    unittest.main()

'''Función	Operación equivalente
assertEqual(a, b)	a == b
assertNotEqual(a, b)	a != b
assertTrue(x)	bool(x) is True
assertFalse(x)	bool(x) is False
assertIs(a, b)	a is b
assertIsNot(a, b)	a is not b
assertIsNone(x)	x is None
assertIsNotNone(x)	x is not None
assertIn(a, b)	a in b
assertNotIn(a, b)	a not in b
assertIsInstance(a, b)	isinstance(a, b)
assertNotIsInstance(a, b)	not isinstance(a, b)'''