import unittest
from decimal import Decimal
from polonomio_grado_2 import PolinomioGrado2 as Polinomio, Excepcion


class Test_raices_polinomio_grado_2(unittest.TestCase):

    def test_uno(self):
        p = Polinomio(1, 2, 3)
        self.assertEqual(p.formulaGeneral(2), [-1+1.41j, -1-1.41j])

    def test_dos(self):
        p = Polinomio(1, 2, 3)
        self.assertEqual(p.formulaGeneral(), [-1+1.414j, -1-1.414j])

    def test_tres(self):
        p = Polinomio(1, 6, 2)
        self.assertEqual(p.formulaGeneral(), [-0.354, -5.646])
    
    def test_cuatro(self):
        p = Polinomio(1, 4, 4)
        self.assertEqual(p.formulaGeneral(), -2)

    def test_excepcion_1(self):
        with self.assertRaises(Excepcion):
            Polinomio(0, 99, 99)

    def test_excepcion_2(self):
        with self.assertRaises(Excepcion):
            Polinomio('a', 'b', 'c')

    def test_excepcion_3(self):
        with self.assertRaises(Excepcion):
            Polinomio(Decimal('Infinity'), 3, 3)
    
    def test_excepcion_4(self):
        with self.assertRaises(Excepcion):
            Polinomio(-1+1j, 2, 2)

if __name__ == '__main__':
    unittest.main()
