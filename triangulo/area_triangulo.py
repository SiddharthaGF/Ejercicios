from math import sqrt, isinf
import string
import numpy

class Excepcion(ValueError):
    def __init__(self, message, * args):
        super(Excepcion, self).__init__(message, * args)

class Triangulo:

    __lados: list[float]
    semiPerimetro: float

    def __init__(self, a, b, c) -> None:
        self.__validarTriangulo([a, b, c])
        
    def __try_parse_float(self, value):
        try:
            return float(value)
        except:
            return None

    def __getSemiperimetro(self, lados: list) -> float:
        return sum(lados)/2

    def __validarTriangulo(self, lados: list) -> None:
        for indice, lado in enumerate(lados):
            aux = self.__try_parse_float(lado)
            if (isinstance(aux, str)):
                raise Excepcion(
                    f'El argumento {indice+1} ({aux}) no puede ser una cadena de caracteres.')
        if (numpy.iscomplex(aux)):
                raise Excepcion(
                    f'El argumento {indice+1} ({aux}) no puede ser un numero complejo.')
        if aux <= 0:
                raise Excepcion(
                    f'El argumento {indice+1} ({aux}) no puede ser un numero negativo')
        if isinf(aux):
                raise Excepcion(
                    f'El argumento {indice+1} ({aux}) no puede ser un numero infinito')
        semi = self.__getSemiperimetro(lados)
        for lado in lados:
            aux = self.__try_parse_float(lado)
            if semi <= aux:
                raise Excepcion("El triangulo no existe")
        self.semiPerimetro = semi
        self.__lados = lados

    def heron(self, decimales=3) -> float:
        parcial = 1
        for lado in self.__lados:
            parcial *= self.semiPerimetro - lado
        return round(sqrt(self.semiPerimetro * parcial), decimales)

    def getA(self) -> float:
        return self.__lados[0]

    def getB(self) -> float:
        return self.__lados[1]

    def getC(self) -> float:
        return self.__lados[2]

    def getLados(self) -> list[float]:
        return self.__lados

    def setA(self, a: float) -> None:
        self.__validarTriangulo([a, self.__lados[1], self.__lados[2]])

    def setB(self, b: float) -> None:
        self.__validarTriangulo([self.__lados[0], b, self.__lados[2]])

    def setC(self, c: float) -> None:
        self.__validarTriangulo([self.__lados[0], self.__lados[1], c])

    def getTipo(self) -> string:
        result = []
        for lado in self.__lados:
            if lado not in result:
                result.append(lado)
        ladosdiferentes = len(result)
        if ladosdiferentes == 3:
            return "escaleno"
        else:
            if ladosdiferentes == 2:
                return "isoceles"
            else:
                return "equilatero"
