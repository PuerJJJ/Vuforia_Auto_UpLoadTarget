# -*- coding: UTF-8 -*-
import  wx
app=wx.App()
window = wx.Frame(None, title = "上传图片", size = (666,666))
panel = wx.Panel(window)
window.Show(True)
app.MainLoop()