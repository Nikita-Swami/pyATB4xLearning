print("-----Start the Program------")
try:
    a = int(input("Enter the num1"))
    b = int(input("Enter the num2"))
    c=a/b
    print("Result div is",c)
except Exception as e:
    print(e)
    print("Please check your inputs, it should not be string or zero")
print("----End of Program----")