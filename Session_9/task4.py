# Write a program which finds out whether a given names is present in a list or not

names = ["aditi" , "harshit", "rohit"]

name = input("Enter the name: ")

nameModified = name.lower()

if nameModified in names:
    print("your name is present in the list")
else:
    print("not present")



