import unittest
from decimal import Decimal
from polonomio_grado_2 import PolinomioGrado2 as polinomio2, Excepcion

class Test_raices_polinomio_grado_2(unittest.TestCase):
    
    def test_uno(self):
        polinomio = polinomio2(1, 2, 3)
        self.assertEqual(polinomio.calcularRaices(2), [-1+1.41j, -1-1.41j])
    
    def test_dos(self):
        polinomio = polinomio2(1, 2, 3)
        self.assertEqual(polinomio.calcularRaices(), [-1+1.414j, -1-1.414j])
        
    def test_tres(self):
        polinomio = polinomio2(1, 6, 2)
        self.assertEqual(polinomio.calcularRaices(), [-0.354, -5.646])
    
    def test_excepcion_1(self): 
        with self.assertRaises(Excepcion):
            polinomio2(0, 99, 99)

    def test_excepcion_2(self): 
        with self.assertRaises(Excepcion):
            polinomio2('a', 'b', 'c')

    def test_excepcion_3(self): 
        num_inf = Decimal('Infinity')
        with self.assertRaises(Excepcion):
            polinomio2(num_inf, num_inf, num_inf)

if __name__ == '__main__':
    unittest.main()
