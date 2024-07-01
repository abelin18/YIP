import random

moves = ['rock', 'paper', 'scissors']

idx = random.randint(0,2)
computer_move = moves[idx]

user_move = input("Your move: ").lower()
print("Computer_move:" + computer_move)
if user_move == computer_move:
    print("It's a tie.")
elif (user_move == "rock" and computer_move == "scissors") or \
     (user_move == "paper" and computer_move == "rock") or \
     (user_move == "scissors" and computer_move == "paper"):
     print("User wins.") 
else:
     print("Computer wins.")