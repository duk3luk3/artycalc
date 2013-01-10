from Tkinter import *
class App:

    def __init__(self, master):

        batteryFrame = Frame(master)
        batteryFrame.grid(row=0,column=0)

        self._batteryFrame = batteryFrame

        Label(batteryFrame, text="Battery Name").grid(row=0,column=0)
        Label(batteryFrame, text="FDC Callsign").grid(row=1,column=0)
        Label(batteryFrame, text="Grid").grid(row=2,column=0)

        
        Entry(batteryFrame).grid(row=0,column=1)

        #self.button = Button(batteryFrame, text="QUIT", fg="red", command=batteryFrame.quit)
        #self.button.grid(row=0,column=1)

        #self.hi_there = Button(batteryFrame, text="Hello", command=self.say_hi)
        #self.hi_there.grid(row=1,column=0)

    def say_hi(self):
        print "hi there, everyone!"

root = Tk()

app = App(root)

root.mainloop()
