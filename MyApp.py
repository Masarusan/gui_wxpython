import mainprogress
import wx
import platform
import system_type


class MyApp(wx.App, system_type.os_type):
    def __init__(self, redirect=False, filename=None):
        self.__systempath_backup = ''
        self.__systempathcsv = ''
        self.__system_type = super().platform_type()
        wx.App.__init__(self, redirect, filename)
        self.frame = mainprogress.wxmainbar(None, title="マージツール", system_type=self.__system_type)


if __name__ == '__main__':
    app = MyApp()
    app.MainLoop()
    print("終了しました。")