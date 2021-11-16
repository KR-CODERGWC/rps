This is a Python version of teh classic rock, paper, scissors game

Below i will explain the logic

 #Import random choice

rps = { #Player choice: [winner, loser] # Create dictionary that sets general rules to the game
    
    #"rock": beats scissors, loses to scissors 
    #"paper": beats rock, loses to scissors
    #"scissors": beats paper, loses to rock
}

def checkGame(player, comp): #function checks players choice and compares to computer
  #if computer = winner index print winning statement
  
  #if computer = loser index print losing statement and what the computer said
  
  #if computer = same as player respoinse rint tie statement 
  
  #return the function 

#Set booleen automatically to make game run

while (gameRunning): #While staement for when to run
 
 #Prompt player input
  #Set computer hand to random values of rps dictionary and specifically choices
  
  #Check if player choice is in rps dictionary choices if yes...
     #Run checkGame
  #If not in rps dictionary choices  set gamerunning to fale and end the game
