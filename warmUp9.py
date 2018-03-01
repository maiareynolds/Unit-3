#Maia Reynolds
#3/1/18
#warmUp8.py - capitalize vowels

text=input("Enter text: ")

for ch in text:
    if ch=="a" or ch=="e" or ch=="i" or ch=="o" or ch=="u":
        print(ch.upper())
    else:
        print(ch.lower())