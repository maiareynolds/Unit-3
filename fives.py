#Maia Reynolds
#2/14/18
#fives.py - prints out multiples of five up to number

number=int(input("Enter a number: "))
if number%5==0:
    number=number+1
else:
    number=number
for i in range(0,number,5):
    print(i)