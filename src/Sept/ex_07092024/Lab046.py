#Polymorphism concept
#Method overiding - Same name in parent and in child class

class Shape:

    def area(self):
        print("Area of shape")

class Rectangle(Shape):

    def __init__(self,length,width):
        self.length = length
        self.width = width

    def area(self):
        print(self.length*self.width)

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        print(3.14*self.radius*self.radius)


Shape1 = Rectangle(3,5)
Shape1.area()

Shape2 = Circle(10)
Shape2.area()