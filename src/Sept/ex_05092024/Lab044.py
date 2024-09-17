#Hierarichal Inheritance

class Father:
    def BHK3(self):
        print("3BHK")

class Arpita(Father):
    def BHK1(self):
        print("1BHK")

class Archana(Father):
    def no_house(self):
        print("No house")

arpita_obj = Arpita()
arpita_obj.BHK1()
arpita_obj.BHK3()

archana_obj = Archana()
archana_obj.BHK3()
archana_obj.no_house()
