idmport wx
class name(wx.Frame):
    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,'Sajid first program',size=(300,200))
        panel=wx.Panel(self)







if __name__=='__main__':
    app=wx.PySimpleApp()
    frame=name(parent=None,id=-1)
    frame.Show()
    app.MainLoop()
