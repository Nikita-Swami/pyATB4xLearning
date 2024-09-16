#Take input and create a class

class Person:
    def __init__(self):
        self.name = input("Enter your name/n")
        self.age = input("Enter your age/n")
        self.phone = input("Enter your phone/n")
        self.occupation = input("Enter your occupation/n")

    def display_information(self):
        print(f"Name is {self.name}")
        print(f"Age is {self.age}")
        print(f"phone is {self.phone}")
        print(f"occupation is {self.occupation}")


#Create an object
person1 = Person()

#call the function
person1.display_information()