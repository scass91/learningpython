#July 15th 2018
#sometimes you wont know how many arguments a function will have
#python allows for an arbitrary number of arguments to be made from the calling
#statement using an asterisk

#positional & arbitrary arguments can be used in combination

def make_pizza(size, *toppings):
    """Summarise the pizza which is about to be made"""
    print("\nMaking a " + str(size) +
         "-inch pizza with the following toppings: ")
    for topping in toppings:
        print("- " + topping)
        
make_pizza(16, "pepperoni")
make_pizza(11, "mushrooms", "salami", "extra cheese")
