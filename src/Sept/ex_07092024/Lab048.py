#Abstraction
#Hide the details and show what is required
from abc import abstractmethod


class Animal:
    def __init__(self,name):
        self.name = name

    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("Bark")

dog = Dog("PP")
dog.sound()