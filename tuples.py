###May 30th 2018
###tuples are similar to lists, however the values stored in tupples are
###immutable, i.e. they cannot be changed
buffet = ("bread", "cereal", "bacon", "sausage", "croissant")
for food in buffet:
    print(food.title())


###Tuple values cannot be changed, the below throws out at error if uncommented
###buffet[0] = "toast"

print("\nOriginal menu:")
for food in buffet:
    print(food.title())

###tuples can be overwritten
buffet = ("falafel", "pancakes", "bacon", "sausage", "croissant")
print("\nNew menu:")
for food in buffet:
    print(food.title())
