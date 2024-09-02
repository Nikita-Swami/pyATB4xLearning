my_shopping_list = ["bread","butter","milk"]
print(my_shopping_list)
print(len(my_shopping_list))

def bring_more_food(my_list):
    #append is used to add new item in existing list
    my_list.append("Cheese")  #append is a function so we use () not =
    return my_list

l = bring_more_food(my_shopping_list)
print (l)