import wx
class name(wx.Frame):
    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,'Sajid first program',size=(300,200))
        panel=wx.Panel(self)
        box=wx.MessageDialog(None,'Testing, is this program working?', 'Git',wx.YES_NO)
        if box.ShowModal() == wx.ID_YES:
            print("this is the write answer")
        elif box.ShowModal() == wx.ID_NO:
            print ("Wrong answer try again")
            print box
if __name__=='__main__':
    app=wx.PySimpleApp()
    frame=name(parent=None,id=-1)
    frame.Show()
    app.MainLoop()
