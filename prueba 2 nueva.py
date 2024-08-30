Number = input("")
guess = 3
invalid = 10
if int(Number) < guess:
    print("your guessed to low")
elif int(Number) > guess:
    print(" you guessed to high")
elif int(Number) == guess:
    print("you guessed the correct number")
if int(Number) > invalid:
    print("youre noob")
