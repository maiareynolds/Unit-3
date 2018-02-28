#Maia Reynolds
#2/28/18
#BetterAdditionGameDemo/py - more loop practice

from random import randint
numCorrect=0
while numCorrect<5:
    num1=randint(-10,10)
    num2=randint(-10,10)
    ans=int(input("What is"+str(num1)+" + "+str(num2)+"? "))
    if ans==num1+num2:
        numCorrect+=1
    else:
        print("Wrong, the Answer is ",num1+num2)