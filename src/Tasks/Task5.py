### Task #5
# - Create a program that takes two numbers as input and prints whether
# the first number is greater than, less than, or equal to the second number.

num1 = float(input("Enter num1"))
num2 = float(input("Enter num2"))

if num1 > num2:
    print("Num1 is greater", num1)
elif num1< num2:
    print("Num2 is greater", num2)
else:
    print("Num1 is equal to Num2")
