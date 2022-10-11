from geometria.triangulo import Triangulo

a = float(input("Ingrese el valor del lado A >> "))
b = float(input("Ingrese el valor del lado B >> "))
c = float(input("Ingrese el valor del lado C >> "))

try:
    t = Triangulo(a, b, c)
    area = t.heron()
    tipo = t.getTipo()

    print(f'El area del triangulo es {area}')
    print(f'Además es de un triangulo {tipo}')
except Exception as e:
    print(f'Ha ocurrido una excepcion: {repr(e)}')
