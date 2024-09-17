#Encapsulation - bind data variable and methods
#Data member - class variable
#Methods - Def function within the class
#from src.Sept.ex_03092024.Lab036 import object_ref


class Car:
    name = None
    password = 123

    def __init__(self):
        print("DC")

    def change_password(self):
        self.password = "New@123"

obj_ref1 = Car()
print(obj_ref1.password)
obj_ref1.change_password()
