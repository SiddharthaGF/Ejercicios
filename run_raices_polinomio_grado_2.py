from numpy import iscomplex
from algebra.polonomio_grado_2 import PolinomioGrado2 as Polinomio

try:

    a = float(input("\033[;36m"+"Ingrese el valor de coeficiente A >> "))
    b = float(input("Ingrese el valor de coeficiente B >> "))
    c = float(input("Ingrese el valor de coeficiente C >> "))
    d = float(input("\033[;35m" + "Ingrese el número de decimales de la respuesta >> "))

    p = Polinomio(a, b, c)
    r = p.formulaGeneral(int(d))
    
    e = f'{a}x² +'
    if b != 0:
        e += f' {b}x +'
    if c != 0:
        e += f' {c}'
    e.replace(' + - ', ' - ')

    print("\033[;37m" + f'\nLas raices del polinomio {e} son:\n')
    n = len(r)
    if n == 1:
        print(f'  -> x = {r[0]}')
    else:
        for i, x in enumerate(r):
            print(f'  -> x{i+1} = {x}')

except Exception as e:

    print("\033[;31m" + f'Ha ocurrido una excepcion: {repr(e)}')

