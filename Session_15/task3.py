# Write a program to read a log file and find whether it contains 'python'




with open("log.txt") as f:
    content = f.read()


if 'python' in content.lower():
    print("yes python is present")
else:
    print("not present")