import random

def format_output(message):
    """Formats the output message with stars."""
    print(f"***** {message} *****")

def get_user_choice():
    """Enter your choice for valid inputs."""
    while True:
            choice = int(input("Enter 1 for Rock, 2 for Paper, 3 for Scissors: "))
            computer_choice = random.choice([1,2,3])
            if choice not in [1, 2, 3]:
                print(format_output("Please enter a valid number between 1 and 3."))
                continue              
            else:
                return choice,computer_choice

def determine_winner(user_choice, computer_choice):
    """Determines the winner of the game."""
    if user_choice == computer_choice:
        format_output("Tie")
    elif (user_choice == 1 and computer_choice == 3) or \
         (user_choice == 2 and computer_choice == 1) or \
         (user_choice == 3 and computer_choice == 2):
        format_output("win")
    else:
        format_output("lose")
    
chos = get_user_choice()
print(chos)

determine_winner(chos[0], chos[1])
