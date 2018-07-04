###July 4th 2018
###remove specific value instances from a list

pets = ['dog', 'cat', 'fish', 'dog', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)
