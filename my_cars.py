#July 25th 2018
#Import multiple classes - Won't work in ATOM, works in IDLE

from car import Car, ElectricCar

my_mercedes = Car("mercedes", "a-class", 2016)
print(my_mercedes.get_descriptive_name())

my_leaf = ElectricCar("nissan", "leaf", 2018)
print(my_leaf.get_descriptive_name())
