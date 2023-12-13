import sys
import random
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


# value = input("Please enter a value: ")
# print(value)

print("")
playerchoice = input("Enter a number:\n1 for Rock\n2 for Paper\n3 for Scissors\n")

player = int(playerchoice)

if player < 1 or player > 3:
    sys.exit("Enter a valid number")

computerchoice = random.choice("123")

computer = int(computerchoice)

print("")
print("You chose " + playerchoice + ".")
print("Python chose " + computerchoice + ".")
print("")

if player == 1 and computer == 3:
    print("😍 You win!")
elif player == 2 and computer == 1:
    print("😍 You win!")
elif player == 3 and computer == 2:
    print("😍 You win!")
elif player == computer:
    print("😐 Tie game")
else:
    print("😒 Python wins")