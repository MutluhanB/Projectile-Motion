from tkinter import *
from matplotlib import pyplot as plt
from ProjectileMotion import *


"""
MainGui class.
"""
class mainGui:

    """
    Function for reading entries and drawing graph with matplotlib.
    """
    def getEntriesAndPlot(self):
        a=self.speedEntry.get()
        b=self.angleEntry.get()
        x,y=throw(int(a),int(b))
        plt.plot(x,y)
        plt.xlabel("Distance(meter)")
        plt.ylabel("(meter)")
        plt.title("Trajectory for launch with initial speed :" + str(a) +" and angle :"+str(b))
        plt.show()

    def __init__(self,master):
        frame1=Frame(master)
        frame1.pack(side="left")

        frame2=Frame(master)
        frame2.pack(side="left")

        frame3=Frame(master)
        frame3.pack(side="left")

        label1=Label(frame1,text="Initial Speed(m/s):")
        label1.pack(side="top",anchor="ne")

        label2=Label(frame1,text="Launch Angle(°):")
        label2.pack(side="top",anchor="ne")

        self.speedEntry=Entry(frame2)
        self.speedEntry.pack(side="top",anchor="ne")

        self.angleEntry=Entry(frame2)
        self.angleEntry.pack(side="bottom",anchor="ne")

        mainButton=Button(frame3,text="Show Trajectory",command=self.getEntriesAndPlot)
        mainButton.pack()




mainWindow=Tk()
a=mainGui(mainWindow)
mainWindow.title("Projectile Motion")
mainWindow.geometry("325x50")
mainWindow.resizable(height=False,width=False)
mainWindow.mainloop()
