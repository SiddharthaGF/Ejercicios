from polonomio_grado_2 import PolinomioGrado2 as Polinomio

a = input("Ingrese el coeficiente de A >> ")
b = input("Ingrese el coeficiente de B >> ")
c = input("Ingrese el coeficiente de C >> ")

try:
    
    p = Polinomio(a, b, c)
    raices = p.calcularRaices()

    p_str = ''

    if a != 0:
        p_str += f'{a}x² +'
    if b != 0:
        p_str += f' {b}x +'
    if c != 0:
        p_str += f' {c}'

    p_str.replace(' + - ', ' - ')

    print(f'Las raices del polinomio {p_str} son: {raices}')
    
except Exception as e:
    
    print(f'Ha ocurrido una excepcion: {repr(e)}')