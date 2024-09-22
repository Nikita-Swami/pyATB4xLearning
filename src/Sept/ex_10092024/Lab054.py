import math
try:
    math.exp(1000) #overflow error
except Exception as e:
    print(e)
    print("Please try to use lower exp value")