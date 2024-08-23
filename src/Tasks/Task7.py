### Task #7
# ✅ Leap Year Checker:
# ![img_1.png](img_1.png)
# Create a program that determines whether a given year is a leap year.
# A leap year is divisible by 4, but not by 100 unless it is also divisible by 400.
# Use an if-else statement to make this determination.

Year = int(input("Enter the Year"))
if Year % 4 == 0 and Year % 100 != 0 :
    print("This is Leap Year")
elif Year % 400 == 0:
    print("This is Leap Year ")
else:
    print("This is not Leap Year")
