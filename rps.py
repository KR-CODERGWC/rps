from random import choice

rps = { #Player choice: [winner, loser]
    "choices": ["rock", "paper", "scissors"], #Possible choices
    "rock": ["scissors", "paper"]
    "paper": ["rock", "scissors"],
    "scissors": ["paper", "rock"]
}

def checkGame(player, comp):
  if(comp == rps[player][0]): #
    print("Congrats, you won!")
  elif(comp == rps[player][1]):
    print("The computer threw {0}".format(comp))#Get computer threw
    print("Sorry, you lose :(")
  else:
    print("There was a tie")
  return

gameRunning = True #Set automatically to make game run
while (gameRunning):
  player = input("Please pick: rock, paper, or scissors") #Player pick hand input
  comp = choice(rps["choices"]) #Computer hand random
  if player in rps["choices"]: #Check if in dictionary
    checkGame(player, comp) #Run checkGame
  else:
    gameRunning = False #End game if choice not in dictionary
