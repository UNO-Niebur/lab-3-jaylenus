#RPS.py
#Name: Jaylen Atsou
#Date: Feburary 8, 2026
#Assignment: Lab 3


import random

def main():
  wins = 0
  ties = 0
  losses = 0
 
  playagain = "Y"
  while playagain == "Y":

    computer = random.choice( ["R", "P", "S"])
    player = input("MAKE YOUR SELECTION! Rock, Paper, or Scissors: ")

    if computer == "R":
      print("Computer chose Rock.")
    elif computer == "P":
      print("Computer chose Paper.")
    else: 
      print("Computer chose Scissors.")

    if player == "Rock":
      print("You chose Rock.")
    elif player == "Paper":
      print("You chose Paper.")
    elif player == "Scissors":
      print("You chose Scissors.")
    else:
      print("ERROR-Invalid Choice!")

    if player == "Rock" and computer == "R":
      print("Tie game!")
      ties = ties + 1
    if player == "Rock" and computer == "P":
      print("You lose!")
      losses = losses + 1
    if player == "Rock" and computer == "S":
      print("You win!")
      wins = wins + 1
    
    if player == "Paper" and computer == "R":
      print("You win!")
      wins = wins + 1
    if player == "Paper" and computer == "P":
      print("Tie game!")
      ties = ties + 1
    if player == "Paper" and computer == "S":
      print("You lose!")
      losses = losses + 1
  
    if player == "Scissors" and computer == "R":
      print("You lose!")
      losses = losses + 1
    if player == "Scissors" and computer == "P":
      print("You win!")
      wins = wins + 1
    if player == "Scissors" and computer == "S":
      print("Tie game!")
      ties = ties + 1

    playagain= input("Would you like to play again?\n(Y or N): ")

  print("Wins \t Ties \t Losses")
  print("---- \t ---- \t ------")
  print(wins, "\t", ties , "\t", losses)

if __name__ == '__main__':
  main()
