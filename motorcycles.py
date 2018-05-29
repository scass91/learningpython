motorcycles = ['honda', 'ducati', 'vespa']
print(motorcycles)


###Amend this list to replace the 0th index with a new string
motorcycles[0] = "suzuki"
print(motorcycles)

###Append the list to include a new item
motorcycles.append('ducati')
print(motorcycles)


###start with a blank list which can be dynamically added to
motorcycles = []
motorcycles.append('ducati')
motorcycles.append('suzuki')
motorcycles.append('vespa')
print(motorcycles)


###inserting a new element into a list at index position 0
motorcycles = ['honda', 'ducati', 'vespa']
motorcycles.insert(0,'suzuki')
print(motorcycles)


###removing an element from a lists - permanently
motorcycles = ['honda', 'ducati', 'vespa']
del motorcycles[0]
print(motorcycles)

###pop an item off of the end of a list
motorcycles = ['honda', 'ducati', 'vespa']
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

###pop an item from anywhere in a list
motorcycles = ['honda', 'ducati', 'vespa']
first_bike = motorcycles.pop(0)
print("The first motorcycle I owned was a " + first_bike.title())

###remove an item by name/Values
motorcycles = ['honda', 'ducati', 'vespa', 'suzuki']
print(motorcycles)
too_expensive = 'ducati'
too_small = 'vespa'
motorcycles.remove(too_expensive)
motorcycles.remove(too_small)
print(motorcycles)
print("\nA " + too_small.title() + " is too small for me.")
print("\nA " + too_expensive.title() + " is too expensive for me.")
