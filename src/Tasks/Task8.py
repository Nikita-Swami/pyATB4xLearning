### Task #8
#✅ Triangle Classifier:
#Write a program that classifies a triangle based on its side lengths.
#Given three input values representing the lengths of the sides,
#determine if the triangle is equilateral (all sides are equal),
#isosceles (exactly two sides are equal), or scalene (no sides are equal).
#Use an if-else statement to classify the triangle.


Side1 = float(input("Enter first side of triangle"))
Side2 = float(input("Enter second side of triangle"))
Side3 = float(input("Enter third side of triangle"))

if Side1 == Side2 and Side2 == Side3 and Side1 == Side3:
    print("This triangle is Equilateral Triangle")
elif Side1 == Side2 and Side1 != Side3 and Side2 != Side3:
    print("This triangle is Isosceles")
elif Side1 != Side2 and Side3 != Side1 and Side2 == Side3:
    print("This triangle is Isosceles")
elif Side1 != Side2 and Side2 != Side3 and Side1 != Side3:
    print("This triangle is Scalene")
