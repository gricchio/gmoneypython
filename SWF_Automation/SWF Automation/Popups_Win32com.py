'''
Created on Oct 13, 2017

@author: riccga
'''
import win32com.client

#Calls the windows script host and diplays whatever is below in green - u"" means unicode (for displaying characters in other lang.)


message_Box = win32com.client.Dispatch("WScript.Shell")
message_Box.Popup(u"Dominic Smells!")