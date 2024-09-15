#Conversion from tuple to set
t =("Testingacademy", "New", "Testingacademy")
print(t)
print(set(t))

#combine two sets -Union
set1 = {1,2,3}
set2 = {4,5,6}
my_set = set1.union(set2)
print(my_set)

#common elements -intersection
set1 ={1,2,3,4,5}
set2 = {4,5,6,7,8}
my_set = set1.intersection(set2)
print(my_set)
my_set = set1.difference(set2)
print(my_set)


set1 ={1,2,3,4,5}
set2 ={2,3,4,8}
subset = set2.issubset(set1)
print(subset)