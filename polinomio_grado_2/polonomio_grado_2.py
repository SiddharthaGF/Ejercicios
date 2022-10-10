from math import isinf, pow, sqrt
from numpy import iscomplex


class Excepcion(ValueError):
    def __init__(self, message, * args):
        super(Excepcion, self).__init__(message, * args)


class PolinomioGrado2:

    __a: float
    __b: float
    __c: float

    def __init__(self, a, b: any = 0, c: any = 0) -> None:
        self.__validarEntradas([a, b, c])
        self.__asignarCoeficientes([a, b, c])

    def __validarEntradas(self, coeficientes: list) -> None:
        for i, coeficiente in enumerate(coeficientes):
            if isinstance(coeficiente,str):
                raise Excepcion(
                    f'El argumento {i+1} ({coeficiente}) no puede ser una cadena de caracteres.')
            if iscomplex(coeficiente):
                raise Excepcion(
                    f'El argumento {i+1} ({coeficiente}) no puede ser un número complejo.')
            if isinf(coeficiente):
                raise Excepcion(
                    f'El argumento {i+1} ({coeficiente}) no puede ser un número infinito')

    def __asignarCoeficientes(self, coeficientes: list) -> None:
        if float(coeficientes[0]) == 0:
            raise Excepcion(
                'El coeficiente "a" no puede ser 0')
        self.__a = float(coeficientes[0])
        self.__b = float(coeficientes[1])
        self.__c = float(coeficientes[2])

    def calcularDiscriminate(self) -> float:
        return pow(self.__b, 2)-4*self.__a*self.__c

    def formulaGeneral(self, ndig: int = 3) -> list[float]:
        discriminate = self.calcularDiscriminate()
        raiz = sqrt(abs(discriminate))
        t1 = -self.__b/(2*self.__a)
        t2 = raiz/(2*self.__a)
        if discriminate == 0:
            return round(t1 + t2, ndig)
        elif discriminate > 0:
            x1 = round(t1 + t2, ndig)
            x2 = round(t1 - t2, ndig)
        else:
            x1 = complex(round(t1, ndig), round(t2, ndig))
            x2 = complex(round(t1, ndig), -round(t2, ndig))
        return [x1, x2]