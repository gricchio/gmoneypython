import os

project_folder = r'C:\Users\gino.ricchio\Desktop\Python Projects\Fantasy'
os.chdir(project_folder)
logins = open("logins.txt", 'r')
logins = logins.split(",")

print(logins)