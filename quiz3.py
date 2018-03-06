#Maia Reynolds
#3/6/18
#quiz.3.py

#part 1
num=-15
while num<=-9:
    print(num)
    num+=1

#part 2
for i in range(50,17,-2):
    print(i)

#part 3
num2=-100
sum=0
while num2<=1000:
    sum=sum+num2
    num2+=2
print(sum)

#part 4
text=input("Enter text: ")
while "alpaca" not in text:
    text=input("Enter text: ")