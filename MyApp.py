import mainprogress
import wx
import platform
import os


class MyApp(wx.App):
    def __init__(self, redirect=False, filename=None):
        self.__systempath_backup = ''
        self.__systempathcsv = ''
        self.__system_type = self.os_type()
        wx.App.__init__(self, redirect, filename)
        self.frame = mainprogress.wxmainbar(None, title="マージツール", system_type=self.__system_type)

    def os_type(self):
        system_os = platform.system()
        os_ver = 'OS:'
        if system_os == 'Windows':
            self.__systempath_backup = 'file_select¥¥backup_file¥¥'
            self.__systempathcsv = 'file_select¥¥csv_file¥¥'
            print(os_ver + system_os)
            return 0
        elif system_os == 'Darwin':
            print(os_ver + system_os)
            return 1
        elif system_os == 'Linux':
            print(os_ver + system_os)
            return 2
        else:
            print(system_os)



if __name__ == '__main__':
    app = MyApp()
    app.MainLoop()
    print("終了しました。")