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
