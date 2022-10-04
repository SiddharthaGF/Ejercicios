from asyncio.windows_events import NULL
import math

class Excepcion(ValueError):
    def __init__(self, message, * args):
        super(Excepcion, self).__init__(message, * args)

class Triangulo:

    __lados: list[float]
    semiPerimetro: float

    def __init__(self, a: float, b: float, c: float) -> None:
        self.__validarTraingulo([a, b, c])

    def __init__(self, lados: list[float]) -> None:
        self.__validarTraingulo(lados)

    def __getSemiperimetro(self, lados: list) -> float:
        return sum(lados)/2

    def __validarTraingulo(self, lados: list) -> None:
        for indice, lado in enumerate(lados):
            if lado <= 0:
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


lados = [5, 5, 5]
triangulo = Triangulo(lados)
area = triangulo.heron(2)
print(f'El area del triangulo es: {area}')
triangulo.setB(7)
area = triangulo.heron(2)
print(f'El area del triangulo es: {area}')
print(triangulo.getLados())
