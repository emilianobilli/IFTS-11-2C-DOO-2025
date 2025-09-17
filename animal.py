from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name, posicion, velocidad):
        self.name      = name 
        self.posicion  = posicion
        self.velocidad = velocidad

    def caminar(self, tiempo):
        self.posicion = self.velocidad * tiempo


class Perro(Animal):
    def __init__(self, name, posicion):
        super().__init__(name, posicion, 2)

    def caminar(self, tiempo):
        print("Que camine tu hermana")

class Dalmata(Perro):
    def __init__(self, name, posicion):
        super().__init__(name, posicion)

class Gato(Animal):
    def __init__(self, name, posicion):
        super().__init__(name, posicion, 1)

class Diputado(Animal):
    pass

p = Perro("Victor", 0)
g = Gato("Pedro", 0)

p.caminar(10)
g.caminar(10)

print(p.posicion, g.posicion)

