#Multiple Inheritance

class Father:
    def father_money(self):
        print(1000)

class Mother:
    def mother_money(self):
        print(100)

class Son(Father,Mother):
    def son_money(self):
        print(500)

sonobj = Son()
sonobj.son_money()
sonobj.mother_money()
sonobj.father_money()