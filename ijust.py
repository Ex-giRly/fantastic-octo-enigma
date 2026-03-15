from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def move(self):
        pass

class Human(Animal):
    def move(self):
        print("I can walk")

class Fish(Animal):
    def move(self):
        print("I can swim")

class Snake(Animal):
    def move(self):
        print("I can slither")

class Kangaroo(Animal):
    def move(self):
        print("I can hop")

animals = [Human(), Fish(), Snake(), Kangaroo()]

for animal in animals:
    animal.move()