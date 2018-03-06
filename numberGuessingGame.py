#Maia Reynolds
#3/5/18
#numberGuessingGame.py - user guesses number

from random import randint
number=randint(1,100)
guess=int(input("Enter a number from 1 to 100: "))
tries=0
while number!=guess:
    if number<guess:
        print("too low")
        tries+=1
        guess=int(input("Enter a number from 1 to 100: "))
    else:
        print("too high")
        tries+=1
        guess=int(input("Enter a number from 1 to 100: "))
print("You got it in"+tries+"tries!")
