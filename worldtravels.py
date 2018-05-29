###world travel goals
locations = ["Vietnam", "Australia", "Madives", "Russia", "China"]

print("Here is the list of places I really would like to go to:")
print(locations)

print("\nIn alphabetical order, I would like to visit:")
print(sorted(locations))

print("\nAgain, as a reminder, here is my original list of destinations:")
print(locations)

print("\nIn reverse alphabetical order, here is where I would like to go:")
print(sorted(locations, reverse=True))

print("\nOnce again, here is my original list:")
print(locations)

print("\nHere is my list in reverse:")
locations.reverse()
print(locations)

print("\nReversing this again gives my original list:")
locations.reverse()
print(locations)

print("\nThis is my list in alphabetical order:")
locations.sort()
print(locations)

print("\nThis is my list in reverse alphabetical order:")
locations.sort(reverse=True)
print(locations)
