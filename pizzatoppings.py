###June 18th 2018
###Use of multiple lists, is an item in list 'x' also in list 'y'?

availiable_toppings = ['mushrooms', 'extra cheese', 'bacon', 'red pepper', 'olives']
requested_toppings = ['mushrooms', 'green pepper', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in availiable_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we don't have " + requested_topping + ".")

print("\nFinished making your pizza!")
