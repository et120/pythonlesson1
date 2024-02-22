# Misc Notes:
# View > Appearance > Panel Position > Right (move terminal to right)
# Ctrl + B (shortcut to hide file tree)


# value = input('Please enter a value:\n') #new line escape character

# print(value)
# import modules
import sys
import random

# Game Start
print("")
player_choice = input("Enter...\n1 for Rock,\n2 for Paper, or\n3 for Scissors:\n\n")

player = int(player_choice)

if player < 1 or player > 3:
    sys.exit("You must enter 1, 2, or 3.")
    
computer_choice = random.choice("123")

computer = int(computer_choice)

print("")
print("You chose " + player_choice + ".")
print("Python chose " + computer_choice + ".")
print("")