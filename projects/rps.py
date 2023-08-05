# rock paper scissors game using random module
import random

def play():
    print("Welcome to Rock Paper Scissors Game")
    print("If you want to quit the game, type 'q'")
    print("Or type 'r' for rock, 'p' for paper, 's' for scissors")
    listOfSelections = ['r', 'p', 's']
    dec = {'r': 'rock', 'p': 'paper', 's': 'scissors'}
    userScore = 0
    computerScore = 0
    draw = 0
    while True:
        user = input("Enter your choice: ").lower()
        if user == 'q':
            break
        if user not in listOfSelections:
            print("Please enter a valid choice")
            continue
        computer = random.choice(listOfSelections)
        if user == computer:
            print(f"It's a tie! Both chose {dec[user]}")
            draw += 1
        elif ((user == 'r' and computer == 's') or (user == 'p' and computer == 'r') or (user == 's' and computer == 'p')):
            print(f"You won! 🎉 You chose '{dec[user]}' and computer chose '{dec[computer]}'")
            userScore += 1
        else: 
            print(f"You lost! You chose '{dec[user]}' and computer chose '{dec[computer]}'")
            computerScore += 1
    print(f"Your wins: {userScore}\nComputer wins: {computerScore}\nDraw: {draw}")

play()


            
