import math
from matplotlib import pyplot as plt


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
    elif(angle==0):
        print("Angle cant be 0")
        input("Press any key to exit.")
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

s=int(input("Initial speed (m/s): "))
a=int(input("Launch angle: "))
x,y=throw(s,a)
plt.plot(x,y)
plt.xlabel("Distance")
plt.ylabel("Altitude")
plt.title("Trajectory for launch with initial speed :" + str(s) +" and angle :"+str(a))
plt.show()
