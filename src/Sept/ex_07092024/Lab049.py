#Static Method
#it belongs to class rather than object

class Mathoperation:
    def div(self,a,b):
        return a/b

    @staticmethod
    def sum(a,b):
        return a+b

obj = Mathoperation()
output = obj.div(10,2)
print(output)
print(Mathoperation.sum(10,5))