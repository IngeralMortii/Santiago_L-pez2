Number = input("Enter a number between 1 and 10")
if (int(Number) == 3):
    print("you guessed the correct number")
elif (int(Number) > 3):
    print("you guessed too high")
    Number = input("Enter a number between 1 and 10")
elif (int(Number) < 3):
    print("you guessed too low")
    Number = input("Enter a number between 1 and 10")
    