from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def hablar(self):
        pass


class Perro(Animal):
    def hablar(self):
        print("Wow Wow")


class Gato(Animal):
    def hablar(self):
        print("Miau")

