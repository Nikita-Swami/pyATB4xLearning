# List
from lib2to3.pygram import python_grammar_no_print_statement

my_list = [1, 2, 3, 4, 5]

print(my_list)
print(len(my_list))
print(my_list[0])
my_list.append(6)
print(my_list)
my_list.extend([7,8,9,10])
print(my_list)


my_list.insert(10,"NS")
print(my_list)
print(len(my_list))
my_list.remove("NS")
print(my_list)
#list have not fixed data

my_copy_list = my_list.copy()
print(my_copy_list)
# No range is required for this loop because range itself provide list
for element in my_list:
    print(element)


