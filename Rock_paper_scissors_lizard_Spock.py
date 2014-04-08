# Rock-paper-scissors-lizard-Spock (RPSLS) is a variant of 
# Rock-paper-scissors that allows five choices. 
# Each choice wins against two other choices, 
# loses against two other choices and ties against itself. 
# Much of RPSLS's popularity is that it has been featured 
# in 3 episodes of the TV series "The Big Bang Theory". 
# The Wikipedia entry for RPSLS 
# (http://en.wikipedia.org/wiki/Rock-paper-scissors-lizard-Spock) 
# gives the complete description of the details of the game

# This project takes as input the string "name", 
# which is one of the rock, paper, scissors, lizard, or Spock.
# The function simulates playing a round of RPSLS by generating 
# its own random number choice from these alternatives and determine
# the winner (i.e. Player versus Computer) using the rules of the game
# as described in the Wikipedia link above.

import random

# Converts the string "name" to a number betweeen 0 and 4
def name_to_number(name):
    if name == "rock":
        name = 0
    elif name == "Spock":
        name = 1
    elif name == "paper":
        name = 2
    elif name == "lizard":
        name = 3
    elif name == "scissors":
        name = 4 
    else:
        print "The name '%s' is not spelled correctly!" % name
    return name          

# Converts a number in the range 0 to 4 into its corresponding name as a string                    
def number_to_name(number):
    if number == 0:
        number = "rock"
    elif number == 1:
        number = "Spock"
    elif number == 2:
        number = "paper"
    elif number == 3:
        number = "lizard"
    elif number == 4:
        number = "scissors" 
    else:
        print "The number you entered must be between 0 and 4."
    return number                       

# Main function                                                        
def rpsls(player_choice):
    print 
    print "Player chooses", player_choice
    player_number = name_to_number(player_choice)
    comp_number = random.randrange(0,4)
    comp_name = number_to_name(comp_number)
    print "Computer chooses", comp_name
    winner = (comp_number - player_number) % 5
    if winner == 1 or winner == 2:
        print "Computer wins!"
    elif winner == 3 or winner == 4:
        print "Player wins!"
    else:
        print "No winner, play again!"

# Tests the code and play!    
def main():
    rpsls("rock")
    rpsls("Spock")
    rpsls("paper")
    rpsls("lizard")
    rpsls("scissors")
    print
    print

# Standard boilerplate to call the main() function.
if __name__ == '__main__':
  main()