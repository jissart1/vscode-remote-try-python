#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file("index.html")


# Specification
# Game rules:
# Rock beats scissors (breaking it).
# Scissors beat paper (cutting it).
# Paper beat rock (wrapping it).
# The minigame is multiplayer and the computer plays the role of your opponent and chooses a random element from the list of elements
# Interaction with the player:
# The console is used to interact with the player.
# The player can choose one of the three options: rock, paper, or scissors.
# The player can choose whether to play again.
# The player should be warned if they enter an invalid option.
# The player is shown their score at the end of the game.
# Validation of user input:
# At each round, the player must enter one of the options in the list and be informed if they won, lost, or tied with the opponent.
# The minigame must handle user inputs, putting them in lowercase and informing the user if the option is invalid.
# By the end of each round, the player must answer whether they want to play again or not.
# The player must be informed of the final score at the end of the game.
# The game must end when the player chooses not to play again.
# The player must be informed if they won or lost the game.
# Generate the code please

from random import randint
from time import sleep
options = ["P", "F", "C"]
LOSS_MESSAGE = "Perdu!"
WIN_MESSAGE = "Gagné!"
TIE_MESSAGE = "Match nul!"

def decide_winner(user_choice, computer_choice):
  print ("Tu as choisi: %s" % user_choice)
  print ("L'ordi joue...")
  sleep(1)
  print ("L'ordi a choisi : %s" % computer_choice)
  user_choice_index = options.index(user_choice)
  computer_choice_index = options.index(computer_choice)
  if user_choice_index == computer_choice_index:
    print (TIE_MESSAGE)
  elif user_choice_index == 0 and computer_choice_index == 2:
    print (WIN_MESSAGE)
  elif user_choice_index == 1 and computer_choice_index == 0:
    print (WIN_MESSAGE)
  elif user_choice_index == 2 and computer_choice_index == 1:
    print (WIN_MESSAGE)
  elif user_choice_index > 2:
    print ("Invalid option!")
    return
  else:
    print (LOSS_MESSAGE)

def play_RPS():
  print ("Pierre , Feuille , Ciseaux !")
  user_choice = input("Choisis P pour Pierre, F pour Feuille ou C pour Ciseaux: ")
  user_choice = user_choice.upper()
  sleep(1)
  computer_choice = options[randint(0,len(options)-1)]
  decide_winner(user_choice, computer_choice)
play_RPS()








 











