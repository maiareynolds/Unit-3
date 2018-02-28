#Maia Reynolds
#2/28/18
#warmUp8.py - sum of numbers divisible by numbers

number=17
sum=0
for number in range(17,100001):
    if number%17==0 and number%3==0 and number%10==0:
        sum+=number
        number+=17
    else:
        number+=17
print(sum)