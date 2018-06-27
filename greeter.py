###June 23rd 2018

###multi-line string, the += operator adds new string to end of prior string
prompt = "If you tell us who you are, we can personalise what you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print("\nHello, " + name + "!")
