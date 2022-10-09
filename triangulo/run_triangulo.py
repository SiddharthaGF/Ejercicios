from area_triangulo import Triangulo

a = input("Ingrese el valor del lado A >> ")
b = input("Ingrese el valor del lado B >> ")
c = input("Ingrese el valor del lado C >> ")

try:
    t = Triangulo(a, b, c)
    area = t.heron()
    tipo = t.getTipo()

    print(f'El area del triangulo es {area}\n')
    print(f'Ademas es de un triangulo {tipo}')
except Exception as e:
    print(f'Ha ocurrido una excepcion: {repr(e)}')
