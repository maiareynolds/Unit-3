#Maia Reynolds
#3/1/18
#dotsDemo.py - dots on screen

from ggame import *

radius=5
blue=Color(0x6495ED,1)
dot=CircleAsset(radius,LineStyle(1,blue),blue)

for i in range(8*radius-1): #row
    for j in range(4*radius):
        Sprite(dot,(radius**2+radius**2*i,radius**2+radius**2*j))

App().run()