import random

ROCK ='r'
PAPER = 'p'
SCISSORS = 's'

emojis = {ROCK: "🤘",  PAPER: "🧻", SCISSORS: "✂"}
choices = tuple(emojis.keys())


def get_user_choice():    
    while True:
        user_choice = input("Please select Rock Paper or Scissors (r/p/s) : ").lower()
        if user_choice in choices:
            return user_choice
        else:
            print("Invalid choice!")

def display_choices(user_choice, computer_choice):
    print(f"You_chose : {emojis[user_choice]}")
    print(f"The computer_chose : {emojis[computer_choice]}")

def determine_winner(user_choice, computer_choice):
        if user_choice == computer_choice:
            print("Draw")
        elif (
            (user_choice == PAPER and computer_choice == ROCK) or
            (user_choice == SCISSORS and computer_choice == PAPER) or
            (user_choice == ROCK and computer_choice == SCISSORS)
            ):
            print("You win")
        else:
            print("You lose")

def play_game():
    while True:   

        user_choice = get_user_choice()
        computer_choice = random.choice(choices)

        display_choices(user_choice, computer_choice)
        determine_winner(user_choice, computer_choice)

        should_continue = input("Continue (y/n): ").lower()
        if should_continue == 'n':
            break

play_game()