###July 6th 2018
###"make a list called sandwich_orders and fill it with the names of
###various sandwiches. Then make an empty list called finished_sandwiches.
###Loop through this list and print a message for each order. As each sandwich
###is made, move it to the list of finished sandwiches. After all
###sandwiches have been made, list them all"

sandwich_orders = ["Tuna sandwich", "Meatball sandwich", "Cheese sandwich"]
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()

    print("I made your " + sandwich + ".")
    finished_sandwiches.append(sandwich)

print("\nThe following sandwiches have been made:")
for sandwich in finished_sandwiches:
    print(sandwich)
