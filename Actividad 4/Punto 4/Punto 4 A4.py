from abc import ABC, abstractmethod

class Equipo:
    def __init__(self, nombre, país):
        self.__nombre = nombre
        self.__país = país
        self.__totalTiempo = 0
        self.__listaCiclistas = []
    
    def getNombre(self):
        return self.__nombre
    
    def setNombre(self, nombre):
        self.__nombre = nombre
    
    def getPaís(self):
        return self.__país
    
    def setPaís(self, país):
        self.__país = país
    
    def añadirCiclista(self, ciclista):
        self.__listaCiclistas.append(ciclista)
    
    def listarEquipo(self):
        for c in self.__listaCiclistas:
            print(c.getNombre())
    
    def buscarCiclista(self):
        nombreCiclista = input("Ingrese el nombre del ciclista: ")
        for c in self.__listaCiclistas:
            if c.getNombre() == nombreCiclista:
                print(c.getNombre())
    
    def calcularTotalTiempo(self):
        for c in self.__listaCiclistas:
            self.__totalTiempo += c.getTiempoAcumulado()
    
    def imprimir(self):
        print("Nombre del equipo =", self.__nombre)
        print("País =", self.__país)
        print("Total tiempo del equipo =", self.__totalTiempo)


class Ciclista(ABC):
    def __init__(self, identificador, nombre):
        self.__identificador = identificador
        self.__nombre = nombre
        self.__tiempoAcumulado = 0
    
    @abstractmethod
    def imprimirTipo(self):
        pass
    
    def getIdentificador(self):
        return self.__identificador
    
    def setIdentificador(self, identificador):
        self.__identificador = identificador
    
    def getNombre(self):
        return self.__nombre
    
    def setNombre(self, nombre):
        self.__nombre = nombre
    
    def getTiempoAcumulado(self):
        return self.__tiempoAcumulado
    
    def setTiempoAcumulado(self, tiempoAcumulado):
        self.__tiempoAcumulado = tiempoAcumulado
    
    def imprimir(self):
        print("Identificador =", self.__identificador)
        print("Nombre =", self.__nombre)
        print("Tiempo Acumulado =", self.__tiempoAcumulado)


class Velocista(Ciclista):
    def __init__(self, identificador, nombre, potenciaPromedio, velocidadPromedio):
        super().__init__(identificador, nombre)
        self.__potenciaPromedio = potenciaPromedio
        self.__velocidadPromedio = velocidadPromedio
    
    def getPotenciaPromedio(self):
        return self.__potenciaPromedio
    
    def setPotenciaPromedio(self, potenciaPromedio):
        self.__potenciaPromedio = potenciaPromedio
    
    def getVelocidadPromedio(self):
        return self.__velocidadPromedio
    
    def setVelocidadPromedio(self, velocidadPromedio):
        self.__velocidadPromedio = velocidadPromedio
    
    def imprimir(self):
        super().imprimir()
        print("Potencia promedio =", self.__potenciaPromedio)
        print("Velocidad promedio =", self.__velocidadPromedio)
    
    def imprimirTipo(self):
        print("Es un velocista")


class Escalador(Ciclista):
    def __init__(self, identificador, nombre, aceleraciónPromedio, gradoRampa):
        super().__init__(identificador, nombre)
        self.__aceleraciónPromedio = aceleraciónPromedio
        self.__gradoRampa = gradoRampa
    
    def getAceleraciónPromedio(self):
        return self.__aceleraciónPromedio
    
    def setAceleraciónPromedio(self, aceleraciónPromedio):
        self.__aceleraciónPromedio = aceleraciónPromedio
    
    def getGradoRampa(self):
        return self.__gradoRampa
    
    def setGradoRampa(self, gradoRampa):
        self.__gradoRampa = gradoRampa
    
    def imprimir(self):
        super().imprimir()
        print("Aceleración promedio =", self.__aceleraciónPromedio)
        print("Grado de rampa =", self.__gradoRampa)

    def imprimirTipo(self):
        print("Es un escalador")


class Contrarrelojista(Ciclista):
    def __init__(self, identificador, nombre, velocidadMáxima):
        super().__init__(identificador, nombre)
        self.__velocidadMáxima = velocidadMáxima
    
    def getVelocidadMáxima(self):
        return self.__velocidadMáxima
    
    def setVelocidadMáxima(self, velocidadMáxima):
        self.__velocidadMáxima = velocidadMáxima
    
    def imprimir(self):
        super().imprimir()
        print("Velocidad máxima =", self.__velocidadMáxima)
    
    def imprimirTipo(self):
        print("Es un contrarrelojista")


if __name__ == "__main__":
    equipo1 = Equipo("Sky", "Estados Unidos")
    velocista1 = Velocista(123979, "Geraint Thomas", 320, 25)
    escalador1 = Escalador(123980, "Egan Bernal", 25, 10)
    contrarrelojista1 = Contrarrelojista(123981, "Jonathan Castroviejo", 120)
    
    equipo1.añadirCiclista(velocista1)
    equipo1.añadirCiclista(escalador1)
    equipo1.añadirCiclista(contrarrelojista1)
    
    velocista1.setTiempoAcumulado(365)
    escalador1.setTiempoAcumulado(385)
    contrarrelojista1.setTiempoAcumulado(370)
    
    equipo1.calcularTotalTiempo()
    equipo1.imprimir()
    equipo1.listarEquipo()
