from Tkinter import *
from ttk import *

class App:

    def __init__(self, master):

        ## Battery Main Frame

        batteryFrame = Frame(master)
        batteryFrame.grid(row=0,column=0)

        self._batteryFrame = batteryFrame

        ## Battery Information

        Label(batteryFrame, text="Battery Name"  ).grid(row=0,column=0)
        Label(batteryFrame, text="FDC Callsign"  ).grid(row=1,column=0)
        Label(batteryFrame, text="Battery Type"  ).grid(row=2,column=0)
        Label(batteryFrame, text="GRID"          ).grid(row=3,column=0)
        Label(batteryFrame, text="ALT"           ).grid(row=4,column=0)
        Label(batteryFrame, text="Dir. of Fire"  ).grid(row=5,column=0)
        Label(batteryFrame, text="Target Prefix" ).grid(row=6,column=0)
        Label(batteryFrame, text="Target # Start").grid(row=7,column=0)
        
        self._bNameEntry = Entry(batteryFrame)
        self._bNameEntry.grid(row=0,column=1)

        self._bCallsignEntry = Entry(batteryFrame)
        self._bCallsignEntry.grid(row=1,column=1)

        self._bTypeEntry = Entry(batteryFrame)
        self._bTypeEntry.grid(row=2,column=1)
        
        self._bGridEntry = Entry(batteryFrame)
        self._bGridEntry.grid(row=3,column=1)
        
        self._bAltEntry = Entry(batteryFrame)
        self._bAltEntry.grid(row=4,column=1)
        
        self._bLayEntry = Entry(batteryFrame)
        self._bLayEntry.grid(row=5,column=1)
        
        self._bTgtPrefixEntry = Entry(batteryFrame)
        self._bTgtPrefixEntry.grid(row=6,column=1)
        
        self._bTgtOffsetEntry = Entry(batteryFrame)
        self._bTgtOffsetEntry.grid(row=7,column=1)

        ## Observer Information

        Label(batteryFrame, text="OBSERVER INFORMATION").grid(row=0,column=4,columnspan=2)
        Label(batteryFrame, text="Select").grid(row=1,column=4)
        Label(batteryFrame, text="Observer").grid(row=2,column=4)
        Label(batteryFrame, text="Observer Grid").grid(row=3,column=4)
        Label(batteryFrame, text="Observer Alt").grid(row=4,column=4)

        self._OSelBox = Combobox(batteryFrame, values=['New Observer'])
        self._OSelBox.current(0)
        self._OSelBox.grid(row=1,column=5)

        self._OCallsignEntry = Entry(batteryFrame)
        self._OCallsignEntry.grid(row=2,column=5)

        self._OGridEntry = Entry(batteryFrame)
        self._OGridEntry.grid(row=3,column=5)

        self._OAltEntry = Entry(batteryFrame)
        self._OAltEntry.grid(row=4,column=5)

        self._OCommitButton = Button(batteryFrame, text="Add / Update")
        self._OCommitButton.grid(row=5,column=5)

        ## Known Points Information

        Label(batteryFrame, text="KNOWN POINTS").grid(row=6,column=4,columnspan=2)
        Label(batteryFrame, text="Select").grid(row=7,column=4)
        Label(batteryFrame, text="Name").grid(row=8,column=4)
        Label(batteryFrame, text="Grid").grid(row=9,column=4)
        Label(batteryFrame, text="Alt").grid(row=10,column=4)

        self._KSelBox = Combobox(batteryFrame, values=['New Known Point'])
        self._KSelBox.current(0)
        self._KSelBox.grid(row=7,column=5)

        self._KCallsignEntry = Entry(batteryFrame)
        self._KCallsignEntry.grid(row=8,column=5)

        self._KGridEntry = Entry(batteryFrame)
        self._KGridEntry.grid(row=9,column=5)

        self._KAltEntry = Entry(batteryFrame)
        self._KAltEntry.grid(row=10,column=5)

        self._KCommitButton = Button(batteryFrame, text="Add / Update")
        self._KCommitButton.grid(row=11,column=5)

        ## Mission Buttons

        self._MGridButton = Button(batteryFrame, text="GRID", width=8)
        self._MGridButton.grid(row=12,column=0)

        self._MPolarButton = Button(batteryFrame, text="POLAR", width=8)
        self._MPolarButton.grid(row=12,column=1)

        self._MShiftButton = Button(batteryFrame, text="SHIFT", width=8)
        self._MShiftButton.grid(row=12,column=2)

        ## Log Text

        self._LogText = Text(batteryFrame,height=8)
        self._LogText.grid(row=13,column=0,columnspan=6,pady=5)


        

        #self.button = Button(batteryFrame, text="QUIT", fg="red", command=batteryFrame.quit)
        #self.button.grid(row=0,column=1)

        #self.hi_there = Button(batteryFrame, text="Hello", command=self.say_hi)
        #self.hi_there.grid(row=1,column=0)

    def say_hi(self):
        print "hi there, everyone!"

root = Tk()

app = App(root)

root.mainloop()
