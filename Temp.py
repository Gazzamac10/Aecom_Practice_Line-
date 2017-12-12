import os
dir = "C:\\temp\Python\Dev\Autodesk Library\Columns and Framing\Structural Framing\Steel\British Standard"
dirlist = os.listdir(dir)

txtfiles = []
for item in dirlist:
    if "txt" in item:
        txtfiles.append(item)

print txtfiles