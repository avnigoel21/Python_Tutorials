# Write a python progarm to rename a file to "renamed_by_python.txt"

import os

oldName = "sample2.txt"
newName = "renamed_by_python.txt"

with open(oldName, 'r') as f:
    content = f.read()

with open(newName , 'w') as f:
    f.write(content)

os.remove(oldName)