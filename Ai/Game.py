#Implement any Game and demonstrate the Game playing strategies


import random
def play_game():
    choices = ["rock", "paper", "scissors"]
    print("Welcome to Rock, Paper, Scissors!")
    print("Type 'rock', 'paper', or 'scissors'. Type 'exit' to quit.")
    while True:
        user_choice = input("You: ").lower()
        if user_choice == 'exit':
            print("Thanks for playing!")
            break
        if user_choice not in choices:
            print("Invalid choice. Try again.")
            continue
        computer_choice = random.choice(choices)
        print(f"Computer: {computer_choice}")
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            print("You win!")
        else:
            print("You lose!")
play_game()
