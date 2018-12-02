import random
while(1):
    a = 0
    word = input("")
    if(word == "quit"):
        quit()
    while(a == 0):
        with open("words.txt") as word_file:
            words = word_file.readlines()
        random_phrase = random.choice(words)
        with open("corrections.txt") as openfile:
            if(random_phrase)in openfile:
                a = 0
            else:
                a = 1
    print(random_phrase)
    print("\nIf correct, type y. If not, type n")
    correct = input("")
    if(correct == "y"):
        with open("corrections.txt", "a") as myfile:
            myfile.write(word+"="+random_phrase+"\n")


#
# myDict = {
# "input": "Output",
# "input2"}
#
#
#