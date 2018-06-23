###June 21st 2018
favourite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
    }

###print("Sarah's favourite language is " +
###    favourite_languages['sarah'].title() +
###    ".")

###loop through each key-value pair to print everyone's fav lang

for name, language in favourite_languages.items():
    print(name.title() + "'s favourite language is " +
        language.title() + ".")


###print a list of names of people who took this poll
###.keys() is optional here
for name in favourite_languages.keys():
    print(name.title())

###print a message for specific people

friends = ['phil', 'sarah']
for name in favourite_languages.keys():
    print(name.title())

    if name in friends:
        print(" Hi " + name.title() +
        ", I see your favourite language is " +
        favourite_languages[name].title() + "!")


###use of keys to see if a specific person has been added to the dictionary
###in this case have they taken the poll as well??

if 'erin' not in favourite_languages.keys():
    print('Erin, please take the poll!')
