class Person:

    ##Attributes
    id = None
    name = None
    age = None
    email = None
    height = None
    gender = None
    phone_no = None
    address = None

##Behaviour
    def talk(self):
        print("I can talk")

    def sleep(self,name):  #arg with no return
        print("I am a method")
        print("Sleep",name)

    def sleep2(self,name): # arg with return
        print("I am a method")
        return None

    def walk(self):
        print("I am walking")

    def walk_return(self):
        return "I am walking"

##create object of class
tushar = Person()
tushar.name = "Tushar"
print(tushar.name)
tushar.talk()