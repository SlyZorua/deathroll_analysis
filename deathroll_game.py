"""
A simple console-based script where two players can "Death Roll" with a custom initial upper bound. Player 1 goes first.
Last Modified: 11/05/2022
By SlyZorua
"""

# Imports
from random import randint

# Set current roll, and player 1 goes first
current_roll = int(input("Select initial roll maximum: "))
current_player = 1

while True:
    # Roll 1-current_roll
    print("Player " + str(current_player) + " is about to roll from 1 to " + str(current_roll))
    current_roll = randint(1,current_roll)
    print("Player " + str(current_player) + " rolled a: " + str(current_roll))
    
    # Break if player rolls a 1
    if current_roll == 1:
        break
    
    # Next players turn
    if current_player == 1:
        current_player = 2
    elif current_player == 2:
        current_player = 1

# Declare winner as the opposite of the player that rolled 1
if current_player == 1:
    winner = 2
elif current_player == 2:
    winner = 1

print("Player " + str(current_player) + " rolled a 1! Player " + str(winner) + " wins!")

i = input("Press any key to exit")