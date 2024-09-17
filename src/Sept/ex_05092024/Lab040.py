#Inheritance

class Father:
    key1 = "1 BHK"

    def car(self):
        print("Father's Car", "ALTO",self.key1)

class Son(Father):
     key2 = "2 BHK"

     def home(self):
         print("2 BHK","home",self.key2)

father_obj = Father()
father_obj.car()

son_obj = Son()
son_obj.car()

