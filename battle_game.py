import random, os, time

def roll_dice(side):
  return random.randint(1, side)

def health():
  health = ((roll_dice(6)*roll_dice(12))/2)+10
  return health

def strength():
  strength = ((roll_dice(6)*roll_dice(12))/2)+12
  return strength

while True:
  print("Welcome to the Dungeon Crawler!")
  print()
  c1name=input("Enter Character name:")
  c1type=input("Enter Character's type:[human, imp, wizard, elf, etc.]")
  print()
  print("Character Name:", c1name)
  print("Character Type:", c1type)
  c1Health=health()
  c1Strength=strength()
  print("Health:", c1Health, "Strength:", c1Strength)
  print()
  print("Are you ready to begin?")
  print()
  print("Who are they battling?")
  print()
  c2name=input("Enter Character name:")
  c2type=input("Enter Character's type:[human, imp, wizard, elf, etc.]")
  print("Character Name:", c2name)
  print("Character Type:", c2type)
  c2Health=health()
  c2Strength=strength()
  print("Health:", c2Health, "Strength:", c2Strength)
  print()
  round=1
  Winner = None
  while True:
    time.sleep(1)
    os.system("clear")
    print("⚔️ BATTLE TIME ⚔️")
    print()
    print("The battle begins!")
    c1Dice = roll_dice(6)
    c2Dice = roll_dice(6)
    difference = abs(c1Strength - c2Strength) + 1
    if c1Dice > c2Dice:
      c2Health -= difference
      if round==1:
        print(c1name, "wins the first blow")
      else:
        print(c1name, "wins round", round)
    elif c2Dice > c1Dice:
      c1Health -= difference
      if round==1:
        print(c2name, "wins the first blow")
      else:
        print(c2name, "wins round", round)
    else:
      print("Their swords clash and they draw round", round)
    print()
    print(c1name)
    print("HEALTH:", c1Health)
    print()
    print(c2name)
    print("HEALTH:", c2Health)
    print()
    if c1Health<=0:
      print(c1name, "has died!")
      winner = c2name
      break
    elif c2Health<=0:
      print(c2name, "has died!")
      winner = c1name
      break
    else:
      print("And they're both standing for the next round")
      round += 1

  time.sleep(1)
  print()
  print(winner, "has won in", round, "rounds")
  print()
  print("⚔️ BATTLE TIME ⚔️")
  
