#Inheitance
#child access all properties of parent but parent has only its properties
#Single Inheritance
class Parent:
    gold = "2KG"

    def BHK2(self):
      print("2BHK")

class Child(Parent):
    def BHK3(self):
        print("3BHK")

child_ob = Child()
print(child_ob.gold)
child_ob.BHK3()
child_ob.BHK2()

