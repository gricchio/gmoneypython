import os
import shutil
import json
import re

log_folder = r'C:\Program Files\Wizards of the Coast\MTGA\MTGA_Data\Logs\Logs'
magic_code_folder = r'C:\Users\Gino\Documents\Python Materials\Magic_code'

#Get latest Log
os.chdir(log_folder)
logs = os.listdir()
newest = max(logs, key= os.path.getctime)
shutil.copyfile(newest,os.path.join(magic_code_folder,'latestlog.txt'))

#extract card library
os.chdir(magic_code_folder)
open('latestlog.txt', 'rt') as myfile

x = myfile.find('[605]')

print(x)
