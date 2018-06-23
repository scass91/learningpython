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

###loop through dictionary to print everyone's fav lang

for name, language in favourite_languages.items():
    print(name.title() + "'s favourite language is " +
        language.title() + ".")
