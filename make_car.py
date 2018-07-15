#July 15th 2018
#write a function which stores information about a car in a dictionary
#the function should always receive a manufacturer & model, with an arbitrary
#number of keyword arguments as well. Call it with required info, plus 2 key
#value pairs. Print the dictionary which is returned

def make_car(manufacturer, model, **vehicle_info):
    """Returns information about a car"""
    car = {}
    car["manufacturer"] = manufacturer
    car["model"] = model

    for key, value in vehicle_info.items():
        car[key] = value
    return car

car = make_car("subaru", "outback", color="red", tow_package=True)
print(car)
