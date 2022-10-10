from math import sqrt, isinf
from numpy import iscomplex


class Excepcion(ValueError):
    def __init__(self, message, * args):
        super(Excepcion, self).__init__(message, * args)


class Triangulo:

    __lados: list[float]
    semiPerimetro: float

    def __init__(self, a, b, c) -> None:
        self.__validarEntradas([a, b, c])
        self.__validarTriangulo([a, b, c])

    def __validarEntradas(self, lados: list):
        for i, lado in enumerate(lados):
            if (isinstance(lado, str)):
                raise Excepcion(
                    f'El argumento {i+1} ({lado}) no puede ser una cadena de caracteres.')
            if (iscomplex(lado)):
                raise Excepcion(
                    f'El argumento {i+1} ({lado}) no puede ser un numero complejo.')
            if isinf(lado):
                raise Excepcion(
                    f'El argumento {i+1} ({lado}) no puede ser un numero infinito')
            if lado <= 0:
                raise Excepcion(
                    f'El argumento {i+1} ({lado}) no puede ser un numero negativo')

    def __getSemiperimetro(self, lados: list) -> float:
        return sum(lados)/2

    def __validarTriangulo(self, lados: list) -> None:
        semi = self.__getSemiperimetro(lados)
        for lado in lados:
            if semi <= lado:
                raise Excepcion("El triangulo no existe")
        self.semiPerimetro = semi
        self.__lados = lados

    def heron(self, decimales: int = 3) -> float:
        parcial = 1
        for lado in self.__lados:
            parcial *= self.semiPerimetro - lado
        return round(sqrt(self.semiPerimetro * parcial), decimales)

    def getTipo(self) -> str:
        result = []
        for lado in self.__lados:
            if lado not in result:
                result.append(lado)
        n = len(result)
        if n == 3:
            return "escaleno"
        elif n == 2:
            return "isoceles"
        else:
            return "equilatero"
