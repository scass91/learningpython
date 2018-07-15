#July 15th 2018
#arbitrary keyword arguments
#double asterisks creates an empty dictionary which adds name value pairs

def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile["first_name"] = first
    profile["last_name"] = last
    #loop through key-value pairs remaining in dictionary user_info
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile("albert", "einstein", location = "princeton",
                                field = "physics")

print(user_profile)
