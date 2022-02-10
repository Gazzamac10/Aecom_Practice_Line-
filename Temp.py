import os
dir = "C:\\Temp"
dirlist = os.listdir(dir)


txtfiles = []
for item in dirlist:
    if "txt" in item:
        txtfiles.append(item)

print (txtfiles)
