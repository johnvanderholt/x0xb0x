from Globals import *
from pattern import Pattern
from GraphicalInterface import *
import wx

class View:

    def __init__(self, controller):
        self.controller = controller
        
        # Create an instance of our customized Frame class - the GUI. (this is the view)
        self.mainWindow = MainWindow(self.controller, "x0xb0x c0ntr0l")
        self.currentPattern = None

    def initialize(self):
        pass

    def destroy(self):
        pass


    ##
    #
    # MODEL --> VIEW PROTOCOL
    #
    ############################



    #
    # True means the serial port is connected, false if it is not.
    #
    def updateSerialStatus(self, state):
        try:
            if state == TRUE:
                self.mainWindow.statusBar.SetStatusText("Serial Port: Connected", 1)
            else:
                self.mainWindow.statusBar.SetStatusText("Serial Port: Disconnected", 1)
        except Exception, e:
            pass
            
    def updateSelectedSerialPort(self, name):
        menuId = self.mainWindow.portMenu.FindItem(name)
        if menuId != wx.NOT_FOUND:
            self.mainWindow.portMenu.Check(menuId, True)

    def updateSerialPortNames(self, names):
        for item in self.mainWindow.portMenu.GetMenuItems():
            self.mainWindow.portMenu.Destroy(item)

        self.mainWindow.portMenu.Append(ID_SERIAL_PORT1, names[0], kind = wx.ITEM_RADIO)
        self.mainWindow.portMenu.Append(ID_SERIAL_PORT2, names[1], kind = wx.ITEM_RADIO)
        self.mainWindow.portMenu.Append(ID_SERIAL_PORT3, names[2], kind = wx.ITEM_RADIO)
        self.mainWindow.portMenu.Append(ID_SERIAL_PORT4, names[3], kind = wx.ITEM_RADIO)

    def updateCurrentPattern(self, pattern):
        self.mainWindow.patternEditGrid.update(pattern)
    
    def updateStatusText(self, string):
        try:
            self.mainWindow.statusBar.SetStatusText(string, 0)
        except Exception, e:
            pass

    def displayModalStatusError(self, string):
        print string
        dlg = wx.MessageDialog(self.mainWindow, string, 'x0xb0x c0ntr0l', wx.OK | wx.ICON_INFORMATION) 
        dlg.ShowModal() 
        dlg.Destroy()
