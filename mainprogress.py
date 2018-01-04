import progress_gui
import wx
import wx.adv
import os
import filecmp
from file_select import select_file
from Merge_resource import merge_resorce


class wxmainbar(progress_gui.MyFrame4, progress_gui.MyFrame2,progress_gui.MyDialog1, merge_resorce):
    def __init__(self, parent, title, system_type):
        progress_gui.MyFrame4.__init__(self, parent , title)
        icon = wx.Icon("ハサミのフリーアイコン.png", wx.BITMAP_TYPE_PNG)
        if system_type == 0:
            self.SetIcon(icon)
        elif system_type == 1:
            self.dock = wx.adv.TaskBarIcon(iconType=wx.adv.TBI_DOCK)
            self.dock.SetIcon(icon)
        self.__path = ""
        self.Show()

    #判定文を追加する
    def exit(self, event):
        self.Close()

    def Okbutton(self, event):
        mg = merge_resorce()

    def Cancelbutton(self, event):
        print("MargeCancel")

    def statusBar_vew(self, event):
        pass

    def find_str(self, event):
        pass

    def window_csv(self, event):
        pass


    def filechooser(self, event):
        self.__path = self.m_filePicker3.GetPath()
        print(self.__path)
        if self.dialog_YES_NO(event):
            select_file.file_selector(self.__path)
            merge_resorce(self.__path)
        else:
            print("バックアップが選択作成されていません")

    def sf_version(self, event):
        dialog = wx.MessageDialog(self, 'Ver.1.0', 'マージツール', style=wx.OK)
        dialog.ShowModal()
        dialog.Destroy()

    def dialog_YES_NO(self, event):
        dialog = wx.MessageDialog(None, 'バックアップを作成しますか？', 'バクアップ',
                                  style=wx.YES_NO | wx.ICON_INFORMATION)
        res = dialog.ShowModal()
        if res == wx.ID_YES:
            print("OK")
            return True
        elif res == wx.ID_NO:
            print("NO")
            return False
        dialog.Destroy()

    def get_path(self):
        return self.__path

    def set_path(self, path):
        self.__path = path
