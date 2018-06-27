###June 27th 2018
###With a flag
prompt = "\nTell me something, I will repeat it back to you:"
prompt += "\nEnter 'quit' to end this program. "

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)
