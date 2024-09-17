#Multilevel Inheritance
#child class access every class
#father access only grandfather and father class
#grandfather only access his own

class Grandfather:

    gold = "24KRT"
    def BHK1(self):
        print("1BHK")

class Father(Grandfather):
     gold1 = "22KRT"
     def BHK2(self):
         print("2BHK")

class Child(Father):
    def BHK3(self):
        print("3BHK")

child_obj1 = Child()
child_obj1.BHK1()
child_obj1.BHK2()
child_obj1.BHK3()
print(child_obj1.gold)
print(child_obj1.gold1)

