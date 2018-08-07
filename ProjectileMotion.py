import math
from matplotlib import pyplot as plt
#Mutluhan Boz 08.2018
"""
Function to calculate Trajectory. Takes speed and launch angle as argument
and returns two seperate list of distances and Altitudes at given time (same index)
"""
def throw(speed,angle):
    posY=0
    posX=0
    xPosList=[]
    yPosList=[]
    timeList=[]
    time=0
    gravity=9.8
    time=0
    if angle == 90:
        velX=0
        velY=speed*math.sin(math.radians(angle))
    else:
        velX=speed*math.cos(math.radians(angle))
        velY=speed*math.sin(math.radians(angle))
    while posY >=0:
        timeList.append(time)
        posY=velY*time+(1/2*-gravity)*time**2
        if posY<0:
            break
        yPosList.append(posY)
        posX=velX*time
        xPosList.append(posX)
        time+=0.1


    return xPosList,yPosList
