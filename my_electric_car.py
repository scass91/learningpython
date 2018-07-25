#July 25th 2018
#Doesnt work in Atom - does work in IDLE

from car import ElectricCar

my_leaf = ElectricCar("nissan", "leaf", 2018)

print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()
