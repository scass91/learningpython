#July 15th 2018
#sometimes you wont know how many arguments a function will have
#python allows for an arbitrary number of arguments to be made from the calling
#statement using an asterisk

def make_pizza(*toppings):
    """Summarise the pizza which is about to be made"""
    print("\nMaking a pizza with the following toppings: ")
    for topping in toppings:
        print("- " + topping)
make_pizza("pepperoni")
make_pizza("mushrooms", "salami", "extra cheese")
