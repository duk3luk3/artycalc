from Tkinter import *
from ttk import *
import ac_battery as B
import ac_rangetables as R

class SolutionFrame:
    def __init__(self, master, controller):
        self._root = master
        self._controller = controller

        f = Frame(master)
        f.grid(row=0,column=0,sticky="NESW")
        self._MainFrame = f

        Label(f, text="BATTERY INFORMATION").grid(row=0,column=0,columnspan=2,sticky="W")

        
        self._SolutionLabel = Label(f,text="Solution")
        self._SolutionLabel.grid(row=1,column=1,sticky="NWSE")
        self._SolutionText = StringVar()
        self._SolutionLabel["textvariable"] = self._SolutionText
        self._SolutionText.set("Solution")

        self._SolutionNextButton = Button(f,text="Next Solution")
        self._SolutionNextButton.grid(row=2,column=1)
        
        self._SolutionPrevButton = Button(f,text="Prev Solution")
        self._SolutionPrevButton.grid(row=2,column=0)

        Label(f, text="MESSAGE TO OBSERVER").grid(row=3,column=0,columnspan=2,sticky="W")

        self._MTOLabel = Label(f,text="MTO")
        self._MTOLabel.grid(row=4,column=1,sticky="NWSE")
        self._MTOText = StringVar()
        self._MTOLabel["textvariable"] = self._MTOText
        self._MTOText.set("MTO")



class AdjustMissionFrame:
    def __init__(self, master, controller):
        self._root = master;
        self._controller = controller

        f = Frame(master)
        f.grid(row=0,column=0,sticky="NESW")
        self._MainFrame = f

        f.columnconfigure(0, weight=1)
        f.columnconfigure(1, weight=1)

        f = Frame(self._MainFrame)
        f.grid(row=1,column=0, sticky="WE")
        self._TargetFrame = f

        f.columnconfigure(1, weight=1)

        Label(f, text="TARGET DESCRIPTION").grid(row=0,column=0,columnspan=2,sticky="W")
        Label(f, text="Target Des:"       ).grid(row=1,column=0,sticky="E")
        Label(f, text="Radius / Width:"   ).grid(row=4,column=0,sticky="E")
        Label(f, text="Length:"           ).grid(row=5,column=0,sticky="E")
        Label(f, text="Attitude:"         ).grid(row=6,column=0,sticky="E")

        self._TargetDesEntry = Entry(f)
        self._TargetDesEntry.grid(row=1,column=1,rowspan=3,sticky="WE")
        self._TargetDes = StringVar()
        self._TargetDesEntry["textvariable"] = self._TargetDes

        self._TargetExtEntry = Entry(f)
        self._TargetExtEntry.grid(row=4,column=1,sticky="WE")
        self._TargetExtent = StringVar()
        self._TargetExtEntry["textvariable"] = self._TargetExtent

        self._TargetLengthEntry = Entry(f)
        self._TargetLengthEntry.grid(row=5,column=1,sticky="WE")
        self._TargetLength = StringVar()
        self._TargetLengthEntry["textvariable"] = self._TargetLength

        self._TargetAttitudeEntry = Entry(f)
        self._TargetAttitudeEntry.grid(row=6,column=1,sticky="WE")
        self._TargetAttitude = StringVar()
        self._TargetAttitudeEntry["textvariable"] = self._TargetAttitude

        f = Frame(self._MainFrame)
        f.grid(row=0,column=1,rowspan=2,sticky="WE")
        self._MethodFrame = f

        f.columnconfigure(1, weight=1)

        Label(f, text="METHOD OF ENGAGEMENT").grid(row=0,column=0,columnspan=2,sticky="W")
        Label(f, text="Danger Close:"       ).grid(row=1,column=0,sticky="E")
        Label(f, text="Notes:"              ).grid(row=2,column=0,sticky="E")
        Label(f, text="Ammunition:"         ).grid(row=5,column=0,sticky="E")
        Label(f, text="Fuze:"               ).grid(row=6,column=0,sticky="E")
        Label(f, text="Fuze-Time:"          ).grid(row=7,column=0,sticky="E")
        Label(f, text="Round Count:"        ).grid(row=8,column=0,sticky="E")
        Label(f, text="Adj. Round Count:"   ).grid(row=9,column=0,sticky="E")
        Label(f, text="Adjust Piece:"       ).grid(row=10,column=0,sticky="E")
        Label(f, text="Sheaf:"              ).grid(row=11,column=0,sticky="E")

        self._MethodDangercloseBox = Checkbutton(f, text="Yes")
        self._MethodDangercloseBox.grid(row=1,column=1,sticky="WE")
        self._MethodDangerclose = IntVar()
        self._MethodDangercloseBox["variable"] = self._MethodDangerclose

        self._MethodNotesEntry = Entry(f)
        self._MethodNotesEntry.grid(row=2,column=1,columnspan=3,sticky="WE")
        self._MethodNotes = StringVar()
        self._MethodNotesEntry["textvariable"] = self._MethodNotes

        self._MethodAmmunitionBox = Combobox(f)
        ##self._MethodAmmunitionBox.current(0)
        self._MethodAmmunitionBox.grid(row=5,column=1,sticky="WE")

        self._MethodFuzeBox = Combobox(f)
        ##self._MethodFuzeBox.current(0)
        self._MethodFuzeBox.grid(row=6,column=1,sticky="WE")
        
        self._MethodFuzetimeEntry = Entry(f)
        self._MethodFuzetimeEntry.grid(row=7,column=1,sticky="WE")
        self._MethodFuzetime = StringVar()
        self._MethodFuzetimeEntry["textvariable"] = self._MethodFuzetime

        self._MethodRoundcountEntry = Entry(f)
        self._MethodRoundcountEntry.grid(row=8,column=1,sticky="WE")
        self._MethodRoundcount = StringVar()
        self._MethodRoundcountEntry["textvariable"] = self._MethodRoundcount

        self._MethodAdjustcountEntry = Entry(f)
        self._MethodAdjustcountEntry.grid(row=9,column=1,sticky="WE")
        self._MethodAdjustcount = StringVar()
        self._MethodAdjustcountEntry["textvariable"] = self._MethodAdjustcount

        self._MethodAdjustpieceEntry = Entry(f)
        self._MethodAdjustpieceEntry.grid(row=10,column=1,sticky="WE")
        self._MethodAdjustpiece = StringVar()
        self._MethodAdjustpieceEntry["textvariable"] = self._MethodAdjustpiece

        self._MethodSheafBox = Combobox(f)
        ##self._MethodSheafBox.current(0)
        self._MethodSheafBox.grid(row=11,column=1,sticky="WE")

        Label(f, text="METHOD OF CONTROL"   ).grid(row=12,column=0,columnspan=2,sticky="W")
        Label(f, text="Method:"             ).grid(row=13,column=0,sticky="E")
        Label(f, text="Time"                ).grid(row=14,column=0,sticky="E")

        self._ControlMethodBox = Combobox(f, values=['Fire when ready','Fire at my command','Time from now','Time on target'])
        self._ControlMethodBox.current(0)
        self._ControlMethodBox.grid(row=13,column=1,sticky="WE")

        self._ControlTimeEntry = Entry(f)
        self._ControlTimeEntry.grid(row=14,column=1,sticky="WE")
        self._ControlTime = StringVar()
        self._ControlTimeEntry["textvariable"] = self._ControlTime

        self._CommitMissionButton = Button(f, text="Adjust Fire")
        self._CommitMissionButton.grid(row=15,column=1)
        
        self._CancelMissionButton = Button(f, text="Cancel")
        self._CancelMissionButton.grid(row=15,column=0)

        # Grid mission
        
        f = Frame(self._MainFrame)
        f.grid(row=0,column=0,sticky="NWSE")
        self._GridFrame = f

        f.columnconfigure(1, weight=1)

        Label(f, text="MISSION GRID REFERENCE").grid(row=0,column=0,columnspan=2)
        Label(f, text="Grid:").grid(row=1,column=0)
        Label(f, text="Alt:").grid(row=2,column=0)

        # Polar mission

        f = Frame(self._MainFrame)
        f.grid(row=0,column=0,sticky="NWSE")
        self._PolarFrame = f

        Label(f, text="MISSION POLAR COORDINATES").grid(row=0,column=0,columnspan=2)
        Label(f, text="Select:"                  ).grid(row=1,column=0)
        Label(f, text="Observer:"                ).grid(row=2,column=0)
        Label(f, text="Observer Grid:"           ).grid(row=3,column=0)
        Label(f, text="Observer Alt:"            ).grid(row=4,column=0)
        Label(f, text="OT Dir:"                  ).grid(row=5,column=0)
        Label(f, text="Range:"                   ).grid(row=6,column=0)
        Label(f, text="Alt Dif:"                 ).grid(row=7,column=0)

        self._POSelBox = Combobox(f)
        ##self._POSelBox.current(0)
        self._POSelBox.grid(row=1,column=1,sticky="WE")
        #self._POSelBox.bind("<<ComboboxSelected>>", self.Observer_Select)

        self._POCallsignEntry = Entry(f)
        self._POCallsignEntry.grid(row=2,column=1,sticky="WE")
        self._POCallsign = StringVar()
        self._POCallsignEntry["textvariable"] = self._POCallsign

        self._POGridEntry = Entry(f)
        self._POGridEntry.grid(row=3,column=1,sticky="WE")
        self._POGrid = StringVar()
        self._POGridEntry["textvariable"] = self._POGrid

        self._POAltEntry = Entry(f)
        self._POAltEntry.grid(row=4,column=1,sticky="WE")
        self._POAlt = StringVar()
        self._POAltEntry["textvariable"] = self._POAlt

        self._POCommitButton = Button(f, text="Add / Update", command=self.PObserver_Commit)
        self._POCommitButton.grid(row=1,column=2,rowspan=2,sticky="WE")

        self._PODirEntry = Entry(f)
        self._PODirEntry.grid(row=5,column=1,sticky="WE")
        self._PODir = StringVar()
        self._PODirEntry["textvariable"] = self._PODir

        self._PORangeEntry = Entry(f)
        self._PORangeEntry.grid(row=6,column=1,sticky="WE")
        self._PORange = StringVar()
        self._PORangeEntry["textvariable"] = self._PORange

        self._PODeltaAltEntry = Entry(f)
        self._PODeltaAltEntry.grid(row=7,column=1,sticky="WE")
        self._PODeltaAlt = StringVar()
        self._PODeltaAltEntry["textvariable"] = self._PODeltaAlt

        # Shift mission

        f = Frame(self._MainFrame)
        f.grid(row=0,column=0,sticky="NWSE")
        self._ShiftFrame = f

        Label(f, text="MISSION SHIFT KNOWN POINT").grid(row=0,column=0,columnspan=2)
        Label(f, text="Select:"                  ).grid(row=1,column=0)
        Label(f, text="OT Dir:"                  ).grid(row=2,column=0)
        Label(f, text="Left/Right:"              ).grid(row=3,column=0)
        Label(f, text="Add/Drop:"                ).grid(row=4,column=0)
        Label(f, text="Up/Down:"                 ).grid(row=5,column=0)


        self._SSelBox = Combobox(f)
        self._SSelBox.grid(row=1,column=1,sticky="WE")

        self._SDirEntry = Entry(f)
        self._SDirEntry.grid(row=2,column=1,sticky="WE")
        self._SDir = StringVar()
        self._SDirEntry["textvariable"] = self._SDir

        self._SLeftEntry = Entry(f)
        self._SLeftEntry.grid(row=3,column=1,sticky="WE")
        self._SLeft = StringVar()
        self._SLeftEntry["textvariable"] = self._SLeft

        self._SAddEntry = Entry(f)
        self._SAddEntry.grid(row=4,column=1,sticky="WE")
        self._SAdd = StringVar()
        self._SAddEntry["textvariable"] = self._SAdd

        self._SUpEntry = Entry(f)
        self._SUpEntry.grid(row=5,column=1,sticky="WE")
        self._SUp = StringVar()
        self._SUpEntry["textvariable"] = self._SUp



    def PObserver_Commit(self):
        print "Observer_Commit"




class App:

    def __init__(self, master):

        self._root = master;

        master.title("A/N GYK 37")

        ## init classes
        self._battery = B.Battery()

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
        self._bName.trace("w", self.BatteryNameChange)

        self._bCallsignEntry = Entry(batteryFrame)
        self._bCallsignEntry.grid(row=1,column=1,sticky="WE")
        self._bCallsign = StringVar()
        self._bCallsignEntry["textvariable"] = self._bCallsign
        self._bCallsign.trace("w", self.BatteryCallsignChange)

        self._bLoadButton = Button(batteryFrame,text="Load...",command=self.LoadButtonClick)
        self._bLoadButton.grid(row=1,column=2)

        self._bSaveButton = Button(batteryFrame,text="Save...",command=self.SaveButtonClick)
        self._bSaveButton.grid(row=2,column=2)

        self._bTypeBox = Combobox(batteryFrame, values = R.gun_names())
        self._bTypeBox.current(0)
        self._bTypeBox.grid(row=2,column=1,sticky="WE")
        self._bTypeBox.bind("<<ComboboxSelected>>", self.BatteryType_Select)
        
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

        self._LogText = Text(master,height=8)
        self._LogText.grid(row=1,column=0,pady=5,sticky="nswe")

        batteryFrame.rowconfigure(13, weight=1)
        batteryFrame.columnconfigure(1, weight=1)
        batteryFrame.columnconfigure(5, weight=1)

        ## Adjust mission Frame

        self._adjustFrame = AdjustMissionFrame(master, self)
        self._solutionFrame = SolutionFrame(master, self)

        batteryFrame.lift()


        ## resizing

        master.rowconfigure(1, weight=1)
        master.columnconfigure(0,weight=1)

        ## logic

    def BatteryNameChange(self, *args):
        self._battery._info[0] = self._bName.get()

    def BatteryCallsignChange(self, *args):
        self._battery._info[1] = self._bCallsign.get()

    def BatteryType_Select(self, event):
        self._battery._info[2] = R.guns.keys()[self._bTypeBox.current()]

    def LoadButtonClick(self):
        print "Load Button"

    def SaveButtonClick(self):
        print "Save Button"


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

        

    #def load(self, file):
        

root = Tk()

app = App(root)

root.mainloop()
