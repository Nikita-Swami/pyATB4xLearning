#Constructor
#to initialise the values of attribute
#Special function in class, __init__()
#It will automatically called when you create an object
#Constructor have no any return type
#self means current object
class Dog:
    name = None
    age = None

    def __init__(self,name,age):
        print("I will be automatically called")
        self.name = name
        self.age = age

    def sleep(self):
        print("Sleeping")
        print("Who is sleeping",self.name,self.age)

dog1 = Dog("Chow",10)
print(dog1.name)
dog1.sleep()