#Task #11 -
#✅ Fibonaci series 0,0+1, 0+1+1, n = 7 0, 1, 2, 3, 5, 8, 13

num= int(input("Enter the number"))
fib=[0,1]+[0]*(num-1)
for i in range(2,num+1):
    fib[i]=fib[i-1]+fib[i-2]
    print("Fibonacci is:", fib)


