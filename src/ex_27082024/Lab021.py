# Decorators in python
def decorators(func):
    def wrapper():
        print("Something is happening before the function is calling")
        func()
        print("Something is calling after the function is calling")
        return wrapper()


# function defination
@decorators
def drive_bike():
    print("I M driving")
    # Call to the function
# l = my_drive()
# print(l)
