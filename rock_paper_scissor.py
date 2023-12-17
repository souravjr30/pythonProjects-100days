import getpass
import random
choices=["rock","paper","scissors"]
playerChoice=str.casefold(getpass.getpass("Rock, paper or Scissors"))
computerChoice=random.choice(choices)
if(playerChoice==computerChoice):
  print("You tied")
elif(playerChoice=="rock" and computerChoice=="paper"):
  print("You lost")
elif(playerChoice=="rock" and computerChoice=="scissors"):
  print("You win")
elif(playerChoice=="paper" and computerChoice=="rock"):
  print("You win")
elif(playerChoice=="paper" and computerChoice=="scissors"):
  print("You lost")
elif(playerChoice=="scissors" and computerChoice=="rock"):
  print("You lost")
elif(playerChoice=="scissors" and computerChoice=="paper"):
  print("You win")
