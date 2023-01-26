#! /usr/bin/env python 
# -*- coding: utf-8 -*- 
import win32gui
from win32.lib import win32con
from win32gui import *
 
titles = set() 
def foo(hwnd,mouse):  

  #if IsWindow(hwnd) and IsWindowEnabled(hwnd) and IsWindowVisible(hwnd):
  if IsWindow(hwnd)  and IsWindowVisible(hwnd):
      a=win32gui.GetWindowText(hwnd)

      print(win32gui.GetWindowText(hwnd))

      if a!='':      

        if 'Program Manager' not in a:
          if '开始' not in a:
              if '管理员' not in a:

                  win32gui.PostMessage(hwnd, win32con.WM_CLOSE, 0, 0)

      titles.add(GetWindowText(hwnd)) 

 
if __name__ == '__main__':
  EnumWindows(foo, 0) 
  lt = [t for t in titles if t] 
  lt.sort() 
  for t in lt: 
    print(t)