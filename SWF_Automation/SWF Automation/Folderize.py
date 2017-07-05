'''
Created on Jan 30, 2017

@author: riccga
'''
import win32com.client
import os
import time 
import shutil


SourceFolder = r'C:\Users\riccga\Desktop\Python Exports\Facility Files\Previous'
current_time = time.strftime("%I:%M:%S")
current_date = time.strftime("%m") + "-" + time.strftime("%d") + "-" + time.strftime("%Y")
destination = r'C:\Users\riccga\Desktop\Python Exports\Folders'


def file_names_folder(path):
    files = []
    for name in os.listdir(path):
        if os.path.isfile(os.path.join(path, name)):
            files.append(name)
    return files

def abs_path_folder(filename):
    filenames = file_names_folder(filename)
    files = []
    for entity in filenames:
        string = os.path.join(SourceFolder,entity)
        files.append(string)
    return files

def add_serverpath(filename):
    filenames = file_names_folder(filename)
    files = []
    for entity in filenames:
        string = os.path.join(Server_location,entity)
        files.append(string)
    return files

def strip_string(string,number):
    header = string[0:number-1]
    return header

def generate_folder_names_slice(path,characters):
    headers = []
    for cpu in file_names_folder(path):   
        slice = strip_string(cpu,characters)
        #print slice #print each name
        headers.append(slice)
    return headers

def create_if_not_exist(path):
    headerpath = os.path.join(SourceFolder,path)
    if not os.path.exists(headerpath):
        os.makedirs(os.path.join(headerpath))
    return

def move_by_slice(i):
    header = i[0:7]
    old_loc = os.path.join(SourceFolder,i)
    #print old_loc
    new_loc = os.path.join(SourceFolder,header,i)
    #print new_loc    
    shutil.move(old_loc,new_loc)
    return

def copy_by_slice(i):
    header = i[0:7]
    old_loc = os.path.join(SourceFolder,i)
    #print old_loc
    new_loc = os.path.join(SourceFolder,header,i)
    #print new_loc    
    shutil.copy(old_loc,new_loc)
    return



#Create Folder Names based on first 7 digits
headers = generate_folder_names_slice(SourceFolder, 8)

#create folders based on headers tags
for header in headers:
    create_if_not_exist(header)
    


for i in file_names_folder(SourceFolder):
    move_by_slice(i)


print "Done ;-)"

    
