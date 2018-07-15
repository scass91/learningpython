#July 15th 2018
#sometimes you wont know how many arguments a function will have
#python allows for an arbitrary number of arguments to be made from the calling
#statement using an asterisk

def make_pizza(*toppings):
    """Print the list of requested toppings"""
    print(toppings)

make_pizza("pepperoni")
make_pizza("mushrooms", "salami", "extra cheese")
