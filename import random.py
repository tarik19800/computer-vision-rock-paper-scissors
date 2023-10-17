import random

def get_computer_choice():
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)
    return computer_choice

def get_user_choice():
    while True:
        user_choice = input("Enter your choice (Rock, Paper, or Scissors): ").strip().capitalize()
        if user_choice in ["Rock", "Paper", "Scissors"]:
            return user_choice
        else:
            print("Invalid choice. Please enter Rock, Paper, or Scissors.")

def get_winner(computer_choice, user_choice):
    if computer_choice == user_choice:
        return "It is a tie!"
    elif (computer_choice == "Rock" and user_choice == "Scissors") or \
         (computer_choice == "Scissors" and user_choice == "Paper") or \
         (computer_choice == "Paper" and user_choice == "Rock"):
        return "You lost"
    else:
        return "You won!"

def play():
    print("Rock, Paper, Scissors Game")
    while True:
        computer_choice = get_computer_choice()
        user_choice = get_user_choice()

        print(f"Computer's choice: {computer_choice}")
        print(f"Your choice: {user_choice}")

        result = get_winner(computer_choice, user_choice)
        print(result)

        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            break

if __name__ == "__main__":
    play()
