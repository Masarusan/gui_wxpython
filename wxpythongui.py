# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Nov  6 2017)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.html

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 767,477 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		
		self.m_statusBar1 = self.CreateStatusBar( 1, wx.STB_SIZEGRIP, wx.ID_ANY )
		bSizer15 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gbSizer2 = wx.GridBagSizer( 2, 3 )
		gbSizer2.SetFlexibleDirection( wx.BOTH )
		gbSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		gSizer15 = wx.GridSizer( 0, 2, 0, 0 )
		
		
		gbSizer2.Add( gSizer15, wx.GBPosition( 20, 20 ), wx.GBSpan( 3, 3 ), wx.EXPAND, 5 )
		
		self.m_treeCtrl4 = wx.TreeCtrl( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.Size( 200,300 ), wx.TR_DEFAULT_STYLE )
		gbSizer2.Add( self.m_treeCtrl4, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_htmlWin5 = wx.html.HtmlWindow( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.Size( 200,300 ), wx.html.HW_SCROLLBAR_AUTO )
		gbSizer2.Add( self.m_htmlWin5, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_searchCtrl4 = wx.SearchCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_searchCtrl4.ShowSearchButton( True )
		self.m_searchCtrl4.ShowCancelButton( False )
		gbSizer2.Add( self.m_searchCtrl4, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_button28 = wx.Button( self.m_panel2, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer2.Add( self.m_button28, wx.GBPosition( 0, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		
		self.m_panel2.SetSizer( gbSizer2 )
		self.m_panel2.Layout()
		gbSizer2.Fit( self.m_panel2 )
		bSizer15.Add( self.m_panel2, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer15 )
		self.Layout()
		self.m_menubar1 = wx.MenuBar( 0 )
		self.m_menu5 = wx.Menu()
		self.m_menuItem1 = wx.MenuItem( self.m_menu5, wx.ID_ANY, u"About", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu5.Append( self.m_menuItem1 )
		
		self.m_menuItem3 = wx.MenuItem( self.m_menu5, wx.ID_ANY, u"Open", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu5.Append( self.m_menuItem3 )
		
		self.m_menuItem2 = wx.MenuItem( self.m_menu5, wx.ID_ANY, u"終了", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu5.Append( self.m_menuItem2 )
		
		self.m_menubar1.Append( self.m_menu5, u"File" ) 
		
		self.m_menu6 = wx.Menu()
		self.m_menubar1.Append( self.m_menu6, u"Edit" ) 
		
		self.m_menu7 = wx.Menu()
		self.m_menubar1.Append( self.m_menu7, u"View" ) 
		
		self.m_menu8 = wx.Menu()
		self.m_menubar1.Append( self.m_menu8, u"Help" ) 
		
		self.SetMenuBar( self.m_menubar1 )
		
		self.m_toolBar1 = self.CreateToolBar( wx.TB_HORIZONTAL, wx.ID_ANY ) 
		self.m_tool1 = self.m_toolBar1.AddLabelTool( wx.ID_ANY, u"tool", wx.NullBitmap, wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
		
		self.m_toolBar1.Realize() 
		
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_MENU, self.dialog, id = self.m_menuItem1.GetId() )
		self.Bind( wx.EVT_MENU, self.open, id = self.m_menuItem3.GetId() )
		self.Bind( wx.EVT_MENU, self.close, id = self.m_menuItem2.GetId() )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def dialog( self, event ):
		event.Skip()
	
	def open( self, event ):
		event.Skip()
	
	def close( self, event ):
		event.Skip()
	

###########################################################################
## Class MyDialog1
###########################################################################

class MyDialog1 ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 227,138 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		
		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
		
		sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"About" ), wx.VERTICAL )
		
		bSizer7 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText2 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Ver1.0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		bSizer7.Add( self.m_staticText2, 0, wx.ALL, 5 )
		
		gSizer7 = wx.GridSizer( 0, 2, 0, 0 )
		
		
		gSizer7.Add( ( 0, 0), 1, wx.ALIGN_BOTTOM|wx.ALL|wx.EXPAND, 5 )
		
		self.m_button13 = wx.Button( sbSizer2.GetStaticBox(), wx.ID_YES, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer7.Add( self.m_button13, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )
		
		
		bSizer7.Add( gSizer7, 1, wx.EXPAND, 5 )
		
		
		sbSizer2.Add( bSizer7, 1, wx.EXPAND, 5 )
		
		
		bSizer3.Add( sbSizer2, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer3 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_button13.Bind( wx.EVT_BUTTON, self.dialogclose )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def dialogclose( self, event ):
		event.Skip()
	

