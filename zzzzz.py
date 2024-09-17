import random

def format_output(message):
    """Formats the output message with stars."""
    return f"***** {message} *****"

def get_user_choice():
    """Prompts the user to enter their choice and checks for invalid inputs."""
    while True:
        try:
            choice = int(input("Enter 1 for Rock, 2 for Paper, 3 for Scissors: "))
            if choice not in [1, 2, 3]:
                print(format_output("Please enter a  valid number between 1 and 3."))
            else:
                return choice
        except ValueError:
            print(format_output("Please enter a number between 1 and 3."))

def determine_winner(user_choice, computer_choice):
    """Determines the winner of the game."""
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 1 and computer_choice == 3) or \
         (user_choice == 2 and computer_choice == 1) or \
         (user_choice == 3 and computer_choice == 2):
        return "You win!"
    else:
        return "You lose!"

def rps_game():
    """Main function to run the Rock-Paper-Scissors game."""
    choices = {1: "Rock", 2: "Paper", 3: "Scissors"}

    # Get the user's choice
    user_choice = get_user_choice()
    user_choice_name = choices[user_choice]

    # Get the computer's choice
    computer_choice = random.randint(1, 3)
    computer_choice_name = choices[computer_choice]

    # Display choices
    print(format_output(f"You chose {user_choice_name}."))
    print(format_output(f"The computer chose {computer_choice_name}."))

    # Determine the winner
    result = determine_winner(user_choice, computer_choice)
    print(format_output(result))

if __name__ == "__main__":
    rps_game()