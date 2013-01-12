from Tkinter import *
from ttk import *
import ac_battery as B

class AdjustMissionFrame:
    def __init__(self, master, controller):
        self._root = master;
        self._controller = controller

        f = Frame(master)
        f.grid(row=0,column=0,sticky="NESW")
        self._MainFrame = f

        f = Frame(self._MainFrame)
        f.grid(row=0,column=1)
        self._TargetFrame

        Label(f, text="TARGET DESCRIPTION").grid(row=0,column=0,columnspan=2)
        Label(f, text="Target Des:"       ).grid(row=1,column=0,sticky="E")
        Label(f, text="Radius / Width:"   ).grid(row=4,column=0,sticky="E")
        Label(f, text="Length:"           ).grid(row=5,column=0,sticky="E")
        Label(f, text="Attitude:"         ).grid(row=6,column=0,sticky="E")

        self._TargetDesEntry = Entry(f)
        self._TargetDesEntry.grid(row=1,column=1,columnspan=3,sticky="NSWE)
        self._TargetDes = StringVar()
        self._TargetDesEntry["textvariable"] = self._TargetDes 

        f = Frame(self._MainFrame)
        f.grid(row=1,column=1,rowspan=2)
        self._MethodFrame = f

        Label(f, text="METHOD OF ENGAGEMENT").grid(row=0,column=0,columnspan=2,sticky="W")
        Label(f, text="Danger Close:"       ).grid(row=1,column=0,sticky="E")
        Label(f, text="Notes:"              ).grid(row=2,column=0,sticky="E")
        Label(f, text="Ammunition:"         ).grid(row=3,column=0,sticky="E")
        Label(f, text="Fuze:"               ).grid(row=4,column=0,sticky="E")
        Label(f, text="Fuze-Time:"          ).grid(row=5,column=0,sticky="E")
        Label(f, text="Round Count:"        ).grid(row=6,column=0,sticky="E")
        Label(f, text="Adj. Round Count:"   ).grid(row=7,column=0,sticky="E")
        Label(f, text="Adjust Piece:"       ).grid(row=8,column=0,sticky="E")
        Label(f, text="Sheaf:"              ).grid(row=9,column=0,sticky="E")

        Label(f, text="METHOD OF CONTROL"   ).grid(row=10,column=0,columnspan=2,sticky="E")
        Label(f, text="Method:"             ).grid(row=11,column=0,sticky="E")
        Label(f, text="Time from Now:"      ).grid(row=12,column=0,sticky="E")
        Label(f, text="Clock Time:"         ).grid(row=13,column=0,sticky="E")

        f = Frame(self._MainFrame)
        f.grid(row=0,column=0)
        self._GridFrame = f

        Label(f, text="MISSION GRID REFERENCE").grid(row=0,column=0,columnspan=2)
        Label(f, text="Grid:").grid(row=1,column=0)
        Label(f, text="Alt:").grid(row=2,column=0)

        f = Frame(self._MainFrame)
        f.grid(row=0,column=0)
        self._PolarFrame = f

        Label(f, text="MISSION POLAR COORDINATES").grid(row=0,column=0,columnspan=2)
        Label(f, text="Select:"                  ).grid(row=1,column=0)
        Label(f, text="Observer:"                ).grid(row=1,column=0)
        Label(f, text="Observer Grid:"           ).grid(row=1,column=0)
        Label(f, text="Observer Alt:"            ).grid(row=1,column=0)
        Label(f, text="OT Dir:"                  ).grid(row=1,column=0)
        Label(f, text="Range:"                   ).grid(row=1,column=0)
        Label(f, text="Alt Dif:"                 ).grid(row=1,column=0)





class App:

    def __init__(self, master):

        self._root = master;

        master.title("A/N GYK 37")

        ##Style().configure('TFrame.border', background="black")

        ## Battery Main Frame

        batteryFrame = Frame(master)
        batteryFrame.grid(row=0,column=0,sticky="nsew")

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
        self._bNameEntry.grid(row=0,column=1,sticky="WE")
        self._bName = StringVar()
        self._bNameEntry["textvariable"] = self._bName

        self._bCallsignEntry = Entry(batteryFrame)
        self._bCallsignEntry.grid(row=1,column=1,sticky="WE")
        self._bCallsign = StringVar()
        self._bCallsignEntry["textvariable"] = self._bCallsign

        self._bTypeEntry = Entry(batteryFrame)
        self._bTypeEntry.grid(row=2,column=1,sticky="WE")
        self._bType = StringVar()
        self._bTypeEntry["textvariable"] = self._bType
        
        self._bGridEntry = Entry(batteryFrame)
        self._bGridEntry.grid(row=3,column=1,sticky="WE")
        self._bGrid = StringVar()
        self._bGridEntry["textvariable"] = self._bGrid
        
        self._bAltEntry = Entry(batteryFrame)
        self._bAltEntry.grid(row=4,column=1,sticky="WE")
        self._bAlt = StringVar()
        self._bAltEntry["textvariable"] = self._bAlt
        
        self._bLayEntry = Entry(batteryFrame)
        self._bLayEntry.grid(row=5,column=1,sticky="WE")
        self._bLay = StringVar()
        self._bLayEntry["textvariable"] = self._bLay
        
        self._bTgtPrefixEntry = Entry(batteryFrame)
        self._bTgtPrefixEntry.grid(row=6,column=1,sticky="WE")
        self._bTgtPrefix = StringVar()
        self._bTgtPrefixEntry["textvariable"] = self._bTgtPrefix
        
        self._bTgtOffsetEntry = Entry(batteryFrame)
        self._bTgtOffsetEntry.grid(row=7,column=1,sticky="WE")
        self._bTgtOffset = StringVar()
        self._bTgtOffsetEntry["textvariable"] = self._bTgtOffset

        ## Observer Information

        self._Observers = []

        Label(batteryFrame, text="OBSERVER INFORMATION").grid(row=0,column=4,columnspan=2)
        Label(batteryFrame, text="Select").grid(row=1,column=4)
        Label(batteryFrame, text="Observer").grid(row=2,column=4)
        Label(batteryFrame, text="Observer Grid").grid(row=3,column=4)
        Label(batteryFrame, text="Observer Alt").grid(row=4,column=4)

        self._OSelBox = Combobox(batteryFrame, values=['New Observer'])
        self._OSelBox.current(0)
        self._OSelBox.grid(row=1,column=5,sticky="WE")
        self._OSelBox.bind("<<ComboboxSelected>>", self.Observer_Select)

        self._OCallsignEntry = Entry(batteryFrame)
        self._OCallsignEntry.grid(row=2,column=5,sticky="WE")
        self._OCallsign = StringVar()
        self._OCallsignEntry["textvariable"] = self._OCallsign

        self._OGridEntry = Entry(batteryFrame)
        self._OGridEntry.grid(row=3,column=5,sticky="WE")
        self._OGrid = StringVar()
        self._OGridEntry["textvariable"] = self._OGrid

        self._OAltEntry = Entry(batteryFrame)
        self._OAltEntry.grid(row=4,column=5,sticky="WE")
        self._OAlt = StringVar()
        self._OAltEntry["textvariable"] = self._OAlt

        self._OCommitButton = Button(batteryFrame, text="Add / Update", command=self.Observer_Commit)
        self._OCommitButton.grid(row=5,column=5,sticky="WE")

        ## Known Points Information
        self._KnownPoints = []

        Label(batteryFrame, text="KNOWN POINTS").grid(row=6,column=4,columnspan=2)
        Label(batteryFrame, text="Select").grid(row=7,column=4)
        Label(batteryFrame, text="Name").grid(row=8,column=4)
        Label(batteryFrame, text="Grid").grid(row=9,column=4)
        Label(batteryFrame, text="Alt").grid(row=10,column=4)

        self._KSelBox = Combobox(batteryFrame, values=['New Known Point'])
        self._KSelBox.current(0)
        self._KSelBox.grid(row=7,column=5,sticky="WE")
        self._KSelBox.bind("<<ComboboxSelected>>", self.KnownPoint_Select)

        self._KCallsignEntry = Entry(batteryFrame)
        self._KCallsignEntry.grid(row=8,column=5,sticky="WE")
        self._KCallsign = StringVar()
        self._KCallsignEntry["textvariable"] = self._KCallsign

        self._KGridEntry = Entry(batteryFrame)
        self._KGridEntry.grid(row=9,column=5,sticky="WE")
        self._KGrid = StringVar()
        self._KGridEntry["textvariable"] = self._KGrid

        self._KAltEntry = Entry(batteryFrame)
        self._KAltEntry.grid(row=10,column=5,sticky="WE")
        self._KAlt = StringVar()
        self._KAltEntry["textvariable"] = self._KAlt

        self._KCommitButton = Button(batteryFrame, text="Add / Update", command=self.KnownPoint_Commit)
        self._KCommitButton.grid(row=11,column=5,sticky="WE")

        ## Mission Buttons

        self._MGridButton = Button(batteryFrame, text="GRID", width=8)
        self._MGridButton.grid(row=12,column=0)

        self._MPolarButton = Button(batteryFrame, text="POLAR", width=8)
        self._MPolarButton.grid(row=12,column=1)

        self._MShiftButton = Button(batteryFrame, text="SHIFT", width=8)
        self._MShiftButton.grid(row=12,column=2)

        ## Log Text

        self._LogText = Text(batteryFrame,height=8)
        self._LogText.grid(row=13,column=0,columnspan=6,pady=5,sticky="nswe")

        batteryFrame.rowconfigure(13, weight=1)
        batteryFrame.columnconfigure(1, weight=1)
        batteryFrame.columnconfigure(5, weight=1)

        ## Grid mission Frame



        ## resizing

        master.rowconfigure(0, weight=1)
        master.columnconfigure(0,weight=1)




    def Observer_Select(self, event):
        if self._OSelBox.current() == 0:
            self._OCallsign.set("")
            self._OGrid.set("")
            self._OAlt.set("")
        else:
            o = self._Observers[self._OSelBox.current()-1]
            self._OCallsign.set(o._name)
            self._OGrid.set(o._grid)
            self._OAlt.set(o._alt)

    def Observer_Commit(self):
        print "Observer commit..."
        if self._OSelBox.current() == 0:
            print "Adding Observer"
            o = B.Point(self._OCallsign.get(), self._OGrid.get(), self._OAlt.get())
            self._Observers.append(o)
            self._OSelBox["values"] = self._OSelBox["values"] + (o._name,)
        else:
            print "Updating Observer"
            idx =  self._OSelBox.current()
            self._Observers[idx-1] = B.Point(self._OCallsign.get(), self._OGrid.get(), self._OAlt.get())
            self._OSelBox["values"] = ('New Observer',) + tuple(o._name for o in self._Observers)
            self._OSelBox.current(idx)

    def KnownPoint_Select(self, event):
        if self._KSelBox.current() == 0:
            self._KCallsign.set("")
            self._KGrid.set("")
            self._KAlt.set("")
        else:
            o = self._KnownPoints[self._KSelBox.current()-1]
            self._KCallsign.set(o._name)
            self._KGrid.set(o._grid)
            self._KAlt.set(o._alt)

    def KnownPoint_Commit(self):
        print "KnownPoint commit..."
        if self._KSelBox.current() == 0:
            print "Adding KnownPoint"
            o = B.Point(self._KCallsign.get(), self._KGrid.get(), self._KAlt.get())
            self._KnownPoints.append(o)
            self._KSelBox["values"] = self._KSelBox["values"] + (o._name,)
        else:
            print "Updating KnownPoint"
            idx =  self._KSelBox.current()
            self._KnownPoints[idx-1] = B.Point(self._KCallsign.get(), self._KGrid.get(), self._KAlt.get())
            self._KSelBox["values"] = ('New Known Point',) + tuple(o._name for o in self._KnownPoints)
            self._KSelBox.current(idx)

        

    def say_hi(self):
        print "hi there, everyone!"

root = Tk()

app = App(root)

root.mainloop()
