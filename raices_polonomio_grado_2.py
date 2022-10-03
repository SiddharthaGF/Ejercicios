import math

class Excepcion(ValueError):
    def __init__(self, message, * args):
        super(Excepcion, self).__init__(message, * args)

class PolinomioGrado2:

    __a: int
    __b: int
    __c: int

    def __init__(self, a: float, b: float, c: float) -> None:
        self.__asignarCoeficientes([a, b, c])

    def __asignarCoeficientes(self, coeficientes: list[float]) -> None:
        if coeficientes[0] == 0:
            raise Excepcion(
                f'El cofeiciente "a" debe ser diferente de 0.')
        self.__a = coeficientes[0]
        self.__b = coeficientes[1]
        self.__c = coeficientes[2]

    def calcularDiscriminate(self) -> float:
        return math.pow(self.__b, 2)-4*self.__a*self.__c

    def calcularRaices(self, decimales: int = 3) -> list[float]:
        discriminate = self.calcularDiscriminate()
        complejo = False
        if (discriminate < 0):
            raiz = math.sqrt(abs(discriminate))
            complejo = True
        else:
            raiz = math.sqrt(discriminate)
        t1 = -self.__b/(2*self.__a)
        t2 = raiz/(2*self.__a)
        if complejo:
            x1 = (complex(round(t1, decimales), round(t2, decimales)))
            x2 = (complex(round(t1, decimales), -round(t2, decimales)))
        else:
            x1 = (round(t1 + t2, decimales))
            x2 = (round(t1 - t2, decimales))
        return [x1, x2]
