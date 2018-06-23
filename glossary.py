###June 21st 2018
###Glossary of works

words = {
    'for': 'construct for doing repetitive tasks',
    'variable': 'a placeholder for some data type',
    'string': 'an array of characters',
    'list': 'an array of some kind of data type',
    'tuple': 'a list of values which cannot change (immutable)',
    'if': 'conditional statement',
    'str()': 'function for converting to string',
    'sorted()': 'function for temporarily sorting of a list',
    'list()': 'function for converting to list',
    }

for word, description in words.items():
    print(word.upper() + ":" + "\n\t" + description + ".\n")
