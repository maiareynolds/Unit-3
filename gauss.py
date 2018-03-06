#Maia Reynolds
#3/5/18
#gauss.py - sum 1-100

i=int(input("Enter a number: "))
i2=int(input("Enter the second number: "))
d=int(input("Enter the difference: "))
sum=0

while i<=i2:
    sum=sum+i
    i+=d
print(sum)