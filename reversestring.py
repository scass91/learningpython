#July 26th 2018
#Attempt to reverse a string - this works in Atom, not in IDLE

def reversestring(s):
    """Reverse a given string"""
    str = ""
    for i in s:
        str = i + str
#return gives no result in ATOM or IDLE
    print str

reversestring("West Ham United")
