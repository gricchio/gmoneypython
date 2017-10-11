import os
path = r'C:\Users\riccga\Desktop\Python Exports\Tagetik\Facility Review Files'

files = []
for name in os.listdir(path):
    if os.path.isfile(os.path.join(path, name)):
        files.append(name)


print files