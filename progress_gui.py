# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Nov  6 2017)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid


###########################################################################
## Class MyFrame4
###########################################################################

class MyFrame4(wx.Frame):

    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=title, pos=wx.DefaultPosition,
                          size=wx.Size(526, 271), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        sbSizer5 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"マージ"), wx.VERTICAL)

        self.m_panel4 = wx.Panel(sbSizer5.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                 wx.TAB_TRAVERSAL)
        bSizer27 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_gauge6 = wx.Gauge(self.m_panel4, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL)
        self.m_gauge6.SetValue(0)
        bSizer27.Add(self.m_gauge6, 1, wx.ALIGN_BOTTOM | wx.ALL, 5)

        gSizer16 = wx.GridSizer(0, 2, 0, 0)

        bSizer27.Add(gSizer16, 1, wx.EXPAND, 5)

        self.m_panel4.SetSizer(bSizer27)
        self.m_panel4.Layout()
        bSizer27.Fit(self.m_panel4)
        sbSizer5.Add(self.m_panel4, 1, wx.EXPAND | wx.ALL, 5)

        bSizer30 = wx.BoxSizer(wx.HORIZONTAL)

        sbSizer7 = wx.StaticBoxSizer(wx.StaticBox(sbSizer5.GetStaticBox(), wx.ID_ANY, u"ファイル選択"), wx.VERTICAL)

        self.m_filePicker3 = wx.FilePickerCtrl(sbSizer7.GetStaticBox(), wx.ID_ANY, u"ファイルのあるディレクトリを選択・・・",
                                               u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize,
                                               wx.FLP_DEFAULT_STYLE)
        sbSizer7.Add(self.m_filePicker3, 0, wx.ALL | wx.EXPAND, 5)

        bSizer30.Add(sbSizer7, 1, wx.EXPAND, 5)

        sbSizer5.Add(bSizer30, 1, wx.EXPAND, 5)

        sbSizer5.Add((0, 0), 1, wx.EXPAND, 5)

        sbSizer5.Add((0, 0), 1, wx.EXPAND, 5)

        sbSizer5.Add((0, 0), 1, wx.EXPAND, 5)

        sbSizer5.Add((0, 0), 1, wx.EXPAND, 5)

        sbSizer5.Add((0, 0), 1, wx.EXPAND, 5)

        self.m_staticline3 = wx.StaticLine(sbSizer5.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                           wx.LI_HORIZONTAL)
        sbSizer5.Add(self.m_staticline3, 0, wx.EXPAND | wx.ALL, 5)

        m_sdbSizer21 = wx.StdDialogButtonSizer()
        self.m_sdbSizer21OK = wx.Button(sbSizer5.GetStaticBox(), wx.ID_OK)
        m_sdbSizer21.AddButton(self.m_sdbSizer21OK)
        self.m_sdbSizer21Cancel = wx.Button(sbSizer5.GetStaticBox(), wx.ID_CANCEL)
        m_sdbSizer21.AddButton(self.m_sdbSizer21Cancel)
        m_sdbSizer21.Realize();

        sbSizer5.Add(m_sdbSizer21, 1, wx.EXPAND, 5)

        self.SetSizer(sbSizer5)
        self.Layout()
        self.m_statusBar2 = self.CreateStatusBar(1, wx.STB_SIZEGRIP, wx.ID_ANY)
        self.m_menubar3 = wx.MenuBar(0)
        self.m_menu9 = wx.Menu()
        self.m_menuItem5 = wx.MenuItem(self.m_menu9, wx.ID_ANY, u"終了", wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menu9.Append(self.m_menuItem5)

        self.m_menubar3.Append(self.m_menu9, u"ファイル")

        self.m_menu10 = wx.Menu()
        self.m_menuItem7 = wx.MenuItem(self.m_menu10, wx.ID_ANY, u"置換", wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menu10.Append(self.m_menuItem7)

        self.m_menubar3.Append(self.m_menu10, u"編集")

        self.m_menu11 = wx.Menu()
        self.m_menuItem8 = wx.MenuItem(self.m_menu11, wx.ID_ANY, u"ビュー", wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menu11.Append(self.m_menuItem8)

        self.m_menubar3.Append(self.m_menu11, u"ツール")

        self.m_menu12 = wx.Menu()
        self.m_menuItem9 = wx.MenuItem(self.m_menu12, wx.ID_ANY, u"バージョン", wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menu12.Append(self.m_menuItem9)

        self.m_menubar3.Append(self.m_menu12, u"ヘルプ")

        self.SetMenuBar(self.m_menubar3)

        self.Centre(wx.BOTH)

        # Connect Events
        self.m_filePicker3.Bind(wx.EVT_FILEPICKER_CHANGED, self.filechooser)
        self.m_sdbSizer21Cancel.Bind(wx.EVT_BUTTON, self.Cancelbutton)
        self.m_sdbSizer21OK.Bind(wx.EVT_BUTTON, self.Okbutton)
        self.m_statusBar2.Bind(wx.EVT_CHAR, self.statusBar_view)
        self.Bind(wx.EVT_MENU, self.exit, id=self.m_menuItem5.GetId())
        self.Bind(wx.EVT_MENU, self.find_str, id=self.m_menuItem7.GetId())
        self.Bind(wx.EVT_MENU, self.window_csv, id=self.m_menuItem8.GetId())
        self.Bind(wx.EVT_MENU, self.sf_version, id=self.m_menuItem9.GetId())

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def filechooser(self, event):
        event.Skip()

    def Cancelbutton(self, event):
        event.Skip()

    def Okbutton(self, event):
        event.Skip()

    def statusBar_view(self, event):
        event.Skip()

    def exit(self, event):
        event.Skip()

    def find_str(self, event):
        event.Skip()

    def window_csv(self, event):
        event.Skip()

    def sf_version(self, event):
        event.Skip()


###########################################################################
## Class MyFrame2
###########################################################################

class MyFrame2(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"CSV比較表", pos=wx.DefaultPosition, size=wx.Size(1015, 210),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer15 = wx.BoxSizer(wx.HORIZONTAL)

        sbSizer5 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"変更前"), wx.VERTICAL)

        self.m_grid4 = wx.grid.Grid(sbSizer5.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)

        # Grid
        self.m_grid4.CreateGrid(5, 5)
        self.m_grid4.EnableEditing(True)
        self.m_grid4.EnableGridLines(True)
        self.m_grid4.EnableDragGridSize(False)
        self.m_grid4.SetMargins(0, 0)

        # Columns
        self.m_grid4.EnableDragColMove(False)
        self.m_grid4.EnableDragColSize(True)
        self.m_grid4.SetColLabelSize(30)
        self.m_grid4.SetColLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Rows
        self.m_grid4.EnableDragRowSize(True)
        self.m_grid4.SetRowLabelSize(80)
        self.m_grid4.SetRowLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Label Appearance

        # Cell Defaults
        self.m_grid4.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)
        sbSizer5.Add(self.m_grid4, 0, wx.ALL, 5)

        bSizer15.Add(sbSizer5, 1, wx.EXPAND, 5)

        sbSizer6 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"変更後"), wx.VERTICAL)

        self.m_grid5 = wx.grid.Grid(sbSizer6.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)

        # Grid
        self.m_grid5.CreateGrid(5, 5)
        self.m_grid5.EnableEditing(True)
        self.m_grid5.EnableGridLines(True)
        self.m_grid5.EnableDragGridSize(False)
        self.m_grid5.SetMargins(0, 0)

        # Columns
        self.m_grid5.EnableDragColMove(False)
        self.m_grid5.EnableDragColSize(True)
        self.m_grid5.SetColLabelSize(30)
        self.m_grid5.SetColLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Rows
        self.m_grid5.EnableDragRowSize(True)
        self.m_grid5.SetRowLabelSize(80)
        self.m_grid5.SetRowLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Label Appearance

        # Cell Defaults
        self.m_grid5.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)
        sbSizer6.Add(self.m_grid5, 0, wx.ALL, 5)

        bSizer15.Add(sbSizer6, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer15)
        self.Layout()

        self.Centre(wx.BOTH)

    def __del__(self):
        pass


###########################################################################
## Class MyDialog1
###########################################################################

class MyDialog1(wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"ファイル選択", pos=wx.DefaultPosition, size=wx.Size(268, 155),
                           style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer11 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText5 = wx.StaticText(self, wx.ID_ANY, u"Localizationファイルを選択", wx.DefaultPosition, wx.DefaultSize,
                                           0)
        self.m_staticText5.Wrap(-1)
        bSizer11.Add(self.m_staticText5, 0, wx.ALL, 5)

        bSizer12 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticline2 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
        bSizer12.Add(self.m_staticline2, 0, wx.EXPAND | wx.ALL, 5)

        self.m_filePicker4 = wx.FilePickerCtrl(self, wx.ID_ANY, u"Localizationファイルを選択...", u"Select a file", u"*.*",
                                               wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE)
        bSizer12.Add(self.m_filePicker4, 0, wx.ALL | wx.ALIGN_RIGHT | wx.EXPAND, 5)

        self.m_staticline5 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
        bSizer12.Add(self.m_staticline5, 0, wx.EXPAND | wx.ALL, 5)

        self.m_button11 = wx.Button(self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer12.Add(self.m_button11, 0, wx.ALL | wx.ALIGN_RIGHT, 5)

        bSizer11.Add(bSizer12, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer11)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.m_filePicker4.Bind(wx.EVT_FILEPICKER_CHANGED, self.localization_file)
        self.m_button11.Bind(wx.EVT_BUTTON, self.localizaton_cancel)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def localization_file(self, event):
        event.Skip()

    def localizaton_cancel(self, event):
        event.Skip()
