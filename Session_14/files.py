# Modes of opening a file
# r => reading 
# w => writing
# a => append
# +  => updating


# rb => reading a binary file
# rt or r => reading a text file




# Use open function to read the content of the file
# f = open('abc.txt' , 'r')
f = open('abc.txt') # by default the mode is r
data = f.read()
data = f.read(6) # reads first 6 characters from the file
print(data)
f.close()
