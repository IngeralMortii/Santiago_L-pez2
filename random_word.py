import random
my_word = random.choice(['python', 'java', 'javascript', 'ruby', 'html', 'css'])
print(my_word)
while True :
    word = input ("choose a word from the list : 'python', 'java', 'javascript', 'ruby', 'html', 'css' : ")
    if (word) == "quit" :
        break
    else:
        if (word) ==my_word:
            print("you guessed the correct word")
            break
        elif (word) == ("choose a world of this list : 'python', 'java', 'javascript', 'ruby', 'html', 'css'") :
            print("")
        else :
            print("your word is not in the list or is not correct")
            