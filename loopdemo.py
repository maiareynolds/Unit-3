#Maia Reynolds
#2/14/18
#loopdemo.py - using for and while loops

""" #triple quotes comments out part
#I love computer science 5 times
for i in range(1,6): #only runs 5 times, doesn't do last # , could do 2 and 7, etc.
    print("I <3 Computer Science")
"""
"""
#Counts from 1 to ten
for i in range(1,11):
    print(i)
"""
"""
#Count from 27 to 43 by 2s
for i in range(27,44,2): #last # is by what number...
    print(i)
"""
"""
#add up numbers from 1 to 5
total=0
for i in range(1,6):
    total=total+i
print(total)
"""
#WHILE LOOPS
total=0
i=1
while i<=5:
    total=total+i
    i+=1
print(total)