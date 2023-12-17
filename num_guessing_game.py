import random
myNum=random.randrange(1,1000000)
print("Guess a number between 1 and 1000000")
userNum=int(input("> "))
while True: 
  if userNum==myNum:
    print("You guessed it!")
    break
  elif userNum>myNum:
    print("Too high!")
    userNum=int(input("> "))
    if userNum==myNum:
      print("You guessed it!")
      break
    elif userNum>myNum:
      print("Too high!")
      userNum=int(input("> "))
    elif userNum<myNum:
      print("Too low!")
      userNum=int(input("> "))
  elif userNum<myNum:
    print("Too Low!!")
    userNum=int(input("> "))
    if userNum==myNum:
      print("You guessed it!")
      break
    elif userNum>myNum:
      print("Too high!")
      userNum=int(input("> "))
    elif userNum<myNum:
      print("Too low!")
      userNum=int(input("> "))
