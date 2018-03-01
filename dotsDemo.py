#Maia Reynolds
#3/1/18
#dotsDemo.py - dots on screen

from ggame import *
blue=Color(0x6495ED,1)
dot=CircleAsset(5,LineStyle(1,blue),blue)

for i in range(39): #row
    for j in range(20):
        Sprite(dot,(25+25*i,25+25*j))

App().run()