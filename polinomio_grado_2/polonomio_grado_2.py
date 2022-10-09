from math import isinf, pow, sqrt
from numpy import iscomplex

class Excepcion(ValueError):
    def __init__(self, message, * args):
        super(Excepcion, self).__init__(message, * args)

class PolinomioGrado2:

    __a: float
    __b: float
    __c: float

    def __init__(self, a, b, c) -> None:
        self.__validarEntradas([a, b, c])
        self.__asignarCoeficientes([a, b, c])
        
    def __try_parse_float(self, value):
        try:
            return float(value)
        except:
            return None

    def __validarEntradas(self, coeficientes: list):
        for indice, coeficiente in enumerate(coeficientes):
            aux = self.__try_parse_float(coeficiente)
            if aux is None:
                raise Excepcion(
                    f'El argumento {indice+1} debe ser numerico.')
            if iscomplex(aux):
                raise Excepcion(
                    f'El argumento {indice+1} ({aux}) no puede ser un numero complejo.')
            if isinf(aux):
                raise Excepcion(
                    f'El argumento {indice+1} ({aux}) no puede ser un numero infinito')
        if float(coeficientes[0]) == 0:
            raise Excepcion(
                'El coeficiente "a" no puede ser 0')

    def __asignarCoeficientes(self, coeficientes: list) -> None:
        self.__a = float(coeficientes[0])
        self.__b = float(coeficientes[1])
        self.__c = float(coeficientes[2])

    def calcularDiscriminate(self) -> float:
        return pow(self.__b, 2)-4*self.__a*self.__c

    def calcularRaices(self, decimales: int = 3) -> list[float]:
        discriminate = self.calcularDiscriminate()
        complejo = False
        if (discriminate < 0):
            raiz = sqrt(abs(discriminate))
            complejo = True
        else:
            raiz = sqrt(discriminate)
        t1 = -self.__b/(2*self.__a)
        t2 = raiz/(2*self.__a)
        if complejo:
            x1 = (complex(round(t1, decimales), round(t2, decimales)))
            x2 = (complex(round(t1, decimales), -round(t2, decimales)))
        else:
            x1 = (round(t1 + t2, decimales))
            x2 = (round(t1 - t2, decimales))
        return [x1, x2]
