import random

throws = ["Rock", "Paper", "Scissors"]

while True:
    player = input("Rock, Paper, Scissors (or 'exit' to end): ").capitalize()
    
    if player.lower() == 'exit':
        print("Thanks for playing! Have a Great One.")
        break
    
    if player not in throws:
        print("Invalid input. Please enter Rock, Paper, or Scissors.")
        continue

    computer = random.choice(throws)

    print("Computer chose:", computer)

    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!")
        else:
            print("You win!")
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!")
        else:
            print("You win!")
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose!")
        else:
            print("You win!")
