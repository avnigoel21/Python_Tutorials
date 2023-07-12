# write a program to find out whether a file is identical & matches the content of another file.

file1 = 'this.txt'
file2 = 'wipe.txt'

with open(file1, 'r') as f:
    content1 = f.read()

with open(file2, 'r') as f:
    content2 = f.read()

if content1 == content2:
    print("Files are identical")
else:
    print("not identical")