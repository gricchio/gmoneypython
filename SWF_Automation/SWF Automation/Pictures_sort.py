'''
Created on Apr 21, 2017

@author: RiccGA
'''
import os
import shutil
import datetime
import time



class filestructure(object):
    def __init__(self,path):
        self.path = path
        self.filesnames = []
        for name in os.listdir(self.path):
            if os.path.isfile(os.path.join(path,name)):
                self.filesnames.append(name)
        self.filelocations = []
        for name in self.filesnames:
            string = os.path.join(sourcefolder,name)
            self.filelocations.append(string)
        self.folders = []
        for name in os.listdir(path):
            if os.path.isdir(name):
                self.folders.append(name)

        self.folderpaths = []
        for folder in self.folders:
            string = os.path.join(path,folder)
            self.folderpaths.append(string)

def get_date(object):
    epoch = time.gmtime(os.path.getmtime((object)))
    header = time.strftime("%b %Y", epoch)
    return header

def copy_by_item(i):
    old_loc = i
    new_loc = os.path.join(destination,head)    
    shutil.copy(old_loc,new_loc)
    return
def copy_folder(i, name):
    old_loc = i
    Folder_name = name
    new_loc = os.path.join(destination, head, name) 
    shutil.copytree(old_loc,new_loc)
    return


sourcefolder = r'C:\Users\riccga\Desktop\Python Exports\Picture Sort'
destination = r'C:\Users\riccga\Desktop\Python Exports\Picture Sort\Export'

if not os.path.exists(destination):
    os.mkdir(destination)

os.chdir(sourcefolder)
root = filestructure(sourcefolder)

folderstoscan = root.folderpaths
files = []
filename = []

for folder in folderstoscan:
    filelist = os.listdir(folder)
    print filelist
    for file in filelist:
        fuller = os.path.join(folder,file)
        files.append(fuller)
        filename.append(file)

os.chdir(destination)

print files

for item in files:
    header = get_date(item)
    if not os.path.exists(header):
        os.mkdir(header)

for (item, names) in zip(files, filename):
    head = get_date(item)
    if os.path.isfile(item):
        copy_by_item(item)
        print "item copied --- " + item
    if os.path.isdir(item):
        copy_folder(item, names)
        print "item copied --- " + item

