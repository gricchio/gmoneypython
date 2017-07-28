
import os

SourceFolder = r'C:\Users\riccga\Desktop\Python Exports\Excel Print'
file_list = []

def list_files(path):
    files = []
    for name in os.listdir(path):
        if os.path.isfile(os.path.join(path, name)):
            files.append(name)
    return files

def add_path(filename):
    filenames = list_files(filename)
    files = []
    for entity in filenames:
        string = os.path.join(SourceFolder,entity)
        files.append(string)
    return files

def add_serverpath(filename):
    filenames = list_files(filename)
    files = []
    for entity in filenames:
        string = os.path.join(Server_location,entity)
        files.append(string)
    return files


for obj in add_path(SourceFolder):
    os.startfile(obj, "print")
    print (obj + ' -- Done') 