# function defined
# * is for multiple number-allow multiple args-it should be declared first

def pizza_lover(*toppings, base):
    print(toppings, base)

    nikita = pizza_lover("panner", "capsicum", "onion", base="thin crust")
