#July 10th 2018
#Write a function called describe_city() that accepts the name of a city and
#its country. Give the parameter country a default value, call it for 3
#cities, at least one of which is not in the default country

def describe_city(city, country = "england"):
    """Display cities & their country"""
    print(city + " is in " + country.title() + ".")

describe_city("London")
describe_city("Birmingham")
describe_city("Glasgow", country = "scotland")
