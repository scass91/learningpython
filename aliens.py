###June 23rd 2018
###Nesting dictionaries

alien_0 = {'colour': 'green', 'points': 5}
alien_1 = {'colour': 'yellow', 'points': 10}
alien_2 = {'colour': 'red', 'points': 15}

###put 3 dictionaries into a list called aliens
aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

###make an empty list for storing aliens
aliens = []

###make 30 green aliens
for alien_number in range(30):
    new_alien = {'colour': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

###modify first 3 aliens to be yellow
for alien in aliens[:3]:
    if alien['colour'] == 'green':
        alien['colour'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

### show the first 5 aliens
for alien in aliens[:5]:
    print(alien)
print("...")

### show how many aliens have been created

print("Total number of aliens: " + str(len(aliens)))
