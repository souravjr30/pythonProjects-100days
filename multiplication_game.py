userNum=int(input("Enter a number: "))
for i in range(1,userNum+1):
    num=i*userNum
    ansNum=int(input("Enter the product of "+str(i)+" and "+str(userNum)+": "))
    if ansNum==num:
      print("Great Work!!")
    else:
      print("Sorry, that's incorrect.")
      print("The correct answer is: ",num)
      break
print("Your score is ",i-1," out of ",userNum)
