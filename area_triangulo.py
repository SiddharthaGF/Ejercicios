from asyncio.windows_events import NULL
from decimal import Decimal
import math
import string

class Excepcion(ValueError):
    def __init__(self, message, * args):
        super(Excepcion, self).__init__(message, * args)

class Triangulo:

    __lados: list[float]
    semiPerimetro: float

    def __init__(self, a:float, b:float, c:float) -> None:
        self.__validarTraingulo([a, b, c])

    def __getSemiperimetro(self, lados: list) -> float:
        return sum(lados)/2

    def __validarTraingulo(self, lados: list) -> None:
        for indice, lado in enumerate(lados):
            if lado <= 0 or lado is Decimal('Infinity'):
                raise Excepcion(
                    f'El argumento {indice+1} ({lado}) debe ser un numero real positivo.')
        semi = self.__getSemiperimetro(lados)
        for lado in lados:
            if semi <= lado:
                raise Excepcion("El triangulo no existe")
        self.semiPerimetro = semi
        self.__lados = lados

    def heron(self, decimales=3) -> float:
        parcial = 1
        for lado in self.__lados:
            parcial *= self.semiPerimetro - lado
        return round(math.sqrt(self.semiPerimetro * parcial), decimales)
    
    def getA(self) -> float:
        return self.__lados[0]
    
    def getB(self) -> float:
        return self.__lados[1]
    
    def getC(self) -> float:
        return self.__lados[2]
    
    def getLados(self) -> list[float]:
        return self.__lados
    
    def setA(self, a: float) -> None:
        self.__validarTraingulo([a, self.__lados[1], self.__lados[2]])
            
    def setB(self, b: float) -> None:
        self.__validarTraingulo([self.__lados[0], b, self.__lados[2]])

    def setC(self, c: float) -> None:
        self.__validarTraingulo([self.__lados[0], self.__lados[1], c])
    
    def getTipo(self)-> string:
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
