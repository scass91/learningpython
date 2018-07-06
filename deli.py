###July 6th 2018
###"make a list called sandwich_orders and fill it with the names of
###various sandwiches. Then make an empty list called finished_sandwiches.
###Loop through this list and print a message for each order. As each sandwich
###is made, move it to the list of finished sandwiches. After all
###sandwiches have been made, list them all
###Make pastrami appear several times in the order list, print a message
###revealing that the deli has run out of pastrami"

sandwich_orders = ["Tuna", "Meatball", "Cheese", "Pastrami", "Chicken",
                    "Pastrami", "Ham"]
finished_sandwiches = []

while "Pastrami" in sandwich_orders:
    print("Sorry, we have run out of Pastrami!")
    sandwich_orders.remove("Pastrami")

while sandwich_orders:
    sandwich = sandwich_orders.pop()

    print("I made your " + sandwich + ".")
    finished_sandwiches.append(sandwich)

print("\nThe following sandwiches have been made:")
for sandwich in finished_sandwiches:
    print(sandwich)
