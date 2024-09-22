try:
    num1 = int(input("Enter the num1"))
    num2 = int(input("Enter the num2"))
    Result = num1/num2
except ValueError as ve:
    print("Value Error, You have entered the string instead we want int")
except ZeroDivisionError as zde:
    print("Zero Div Error, Don't use the Num2 as 0")
else:
    print("Result is",Result)
finally:
    print("This code always executed!!")
