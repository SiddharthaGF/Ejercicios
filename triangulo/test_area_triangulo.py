import unittest
from decimal import Decimal
from area_triangulo import Excepcion, Triangulo


class Test_area_triangulo(unittest.TestCase):

    # aceptacion y calculo del area de un triangulo equilatero
    def test_datos_1(self):
        t = Triangulo(2, 2, 2)
        self.assertEqual(t.heron(), 1.732)

    # aceptacion y calculo del area de un triangulo escaleno
    def test_datos_2(self):
        t = Triangulo(2, 3, 4)
        self.assertEqual(t.heron(), 2.905)

    # aceptacion y calculo del area de un triangulo isoceles con dos cifras significativas
    def test_datos_3(self):
        t = Triangulo(2, 3, 2)
        self.assertEqual(t.heron(2), 1.98)

    def test_datos_4(self):
        t = Triangulo(2, 3, 2)
        self.assertEqual(t.getTipo(), 'isoceles')

    def test_datos_5(self):
        t = Triangulo(4, 3, 5)
        self.assertEqual(t.getTipo(), 'escaleno')

    def test_datos_6(self):
        t = Triangulo(5, 5, 5)
        self.assertEqual(t.getTipo(), 'equilatero')

    # rechazo de numeros complejos
    def test_excepcion_1(self):
        with self.assertRaises(Excepcion):
            Triangulo(2j, 2j, 2j)

    # rechazo de cadenas de caracteres
    def test_excepcion_2(self):
        with self.assertRaises(Excepcion):
            Triangulo('a', 'b', 'c')

    # rechazo de numeros infinitos
    def test_excepcion_3(self):
        num_inf = Decimal('Infinity')  # numero infinito
        with self.assertRaises(Excepcion):
            Triangulo(num_inf, num_inf, num_inf)

    # rechazo de numeros negativos
    def test_excepcion_4(self):
        with self.assertRaises(Excepcion):
            Triangulo(-3, -3, -3)

    # rechazo lado 0
    def test_excepcion_5(self):
        with self.assertRaises(Excepcion):
            Triangulo(0, 5, 5)

    # rechazo triangulo no existentes
    def test_excepcion_6(self):
        with self.assertRaises(Excepcion):
            Triangulo(1, 2, 3)


if __name__ == '__main__':
    unittest.main()
