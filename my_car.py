#July 25th 2018
#import a single class

from car import Car

my_new_car = Car("audi", "a4", 2016)
print(my_new_car.get_descriptive_name())

my_new_car.mileage = 23
my_new_car.read_mileage()
