#Method Overloading
#this is not supported in case of python

class MathUtils(object):
    def add(self,a,b):
        return a+b

    def add(self,a,b,c):
        return a+b+c

math = MathUtils()
print(math.add(2,3,7))