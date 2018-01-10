import progress_gui
import wx
import wx.adv
import os
from file_select import select_file
from Merge_resource import merge_resorce


class wxmainbar(progress_gui.MyFrame4, progress_gui.MyFrame2,progress_gui.MyDialog1, merge_resorce):
    def __init__(self, parent, title, system_type):
        self.frame = progress_gui.MyFrame4.__init__(self, parent , title)
        icon = wx.Icon("ハサミのフリーアイコン.png", wx.BITMAP_TYPE_PNG)
        self.__ostype = system_type
        if system_type == 0:
            self.SetIcon(icon)
        elif system_type == 1:
            self.dock = wx.adv.TaskBarIcon(iconType=wx.adv.TBI_DOCK)
            self.dock.SetIcon(icon)
        self.__path = ""
        self.Show()

    def get_ostype(self):
        return self.__ostype

    #判定文を追加する
    def exit(self, event):
        self.Close()
    #マージ処理へ移行
    def Okbutton(self, event):
        if os.path.isfile(self.get_path()):
            print("ファイルが選択されている")
            mg = merge_resorce()
        else:
            print("ファイルが選択されていません")

    def Cancelbutton(self, event):
        print("MargeCancel")

    def statusBar_view(self, event):
        self.SetStatusText(self.get_path())

    def find_str(self, event):
        pass

    def window_csv(self, event):
        pass

    def filechooser(self, event):
        self.__path = self.m_filePicker3.GetPath()
        self.statusBar_view(event)
        #print(self.__path)
        if self.dialog_YES_NO(event):
            select_file.file_backup(self.__path)
            #merge_resorce(self.__path, self.__ostype)
        else:
            #print("バックアップが作成されていません")
            pass

    def sf_version(self, event):
        dialog = wx.MessageDialog(self, 'Ver.1.0', 'マージツール', style=wx.OK)
        dialog.ShowModal()
        dialog.Destroy()

    def dialog_YES_NO(self, event):
        if os.path.isfile(self.get_path()):
            dialog = wx.MessageDialog(None, 'バックアップを作成しますか？', 'バックアップ',
                                      style=wx.YES_NO | wx.ICON_INFORMATION)
            res = dialog.ShowModal()
            print(self.__path)
            if res == wx.ID_YES:
                print("OK")
                return True
            elif res == wx.ID_NO:
                print("NO")
                return False
            dialog.Destroy()
        else:
            pass

    def get_path(self):
        return self.__path

    def set_path(self, path):
        self.__path = path

