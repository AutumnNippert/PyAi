import re
import random
while(1):
    print("Type a word and I'll respond the correct way\n")
    word = input("")
    with open("corrections.txt") as openfile:
        for line in openfile:
            if(word)in line:
                words = (re.split(':|=', line)[-1])
                random_phrase = random.choice(words)
                print (random_phrase)
    input ("Press [ENTER] to restart...")

    # I made a change
    #REEEEEEEEEEEEEE