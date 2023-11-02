import random

# Function to get the computer's choice (randomly)
def get_computer_choice():
    choices = ["Rock", "Paper", "Scissors"]
    return random.choice(choices)

# Function to get the user's choice
def get_user_choice():
    while True:
        user_input = input("Choose Rock, Paper, or Scissors: ").strip().capitalize()
        if user_input in ["Rock", "Paper", "Scissors"]:
            return user_input
        else:
            print("Invalid choice. Please choose Rock, Paper, or Scissors.")

# Function to determine the winner
def get_winner(computer_choice, user_choice):
    if computer_choice == user_choice:
        return "It is a tie!"
    elif (
        (computer_choice == "Rock" and user_choice == "Scissors")
        or (computer_choice == "Paper" and user_choice == "Rock")
        or (computer_choice == "Scissors" and user_choice == "Paper")
    ):
        return "You lost."
    else:
        return "You won!"

# Function to play the Rock-Paper-Scissors game
def play():
    print("Rock-Paper-Scissors Game")
    
    # Get user's choice
    user_choice = get_user_choice()
    
    # Get computer's choice
    computer_choice = get_computer_choice()
    
    print(f"You chose {user_choice}")
    print(f"Computer chose {computer_choice}")
    
    # Determine the winner
    result = get_winner(computer_choice, user_choice)
    print(result)

if __name__ == "__main":
    play()  # Call the play function to start the game
