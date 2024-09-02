global_b = 12  # global variable


def my_fun():  #define new function
    a = 10  # local variable
    print(a)
    print(global_b)


def fun1(): #define new function
    print(global_b)


my_fun()  #function calling
print(global_b)
fun1()
