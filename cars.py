###June 1st 2018 - if statements!
###if my car is what I am searching for, it should return in all caps
###= single sign sets the values
###== double sign is a true/false checker - CaSe SeNsItIvE

cars = ["bmw", "audi", "ford", "vauxhall"]
for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print(car.title())

###inequality testing != is the not equal operator

car_colour = "grey"

if car_colour != "yellow":
    print("\nThat's the wrong colour!\n")


###checking if a value is in a list
cars = ["bmw", "audi", "ford", "vauxhall"]
new_car = "skoda"

if new_car not in cars:
    print(new_car.title() + " must be a new manufacturer")


###booleans are either true or false

car = "subaru"
print("\nIs car == 'subaru'? I'll predict True")
print(car == "subaru")

car = "alfa romeo"
print("\nIs car =='Fiat'? I'll predict False")
print(car == "Fiat")
