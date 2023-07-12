# Write a program to find out the line number where python is present in task3.py

content = True
i = 1
with open("log.txt") as f:

    while content:
        content = f.readline()
        
        if 'python' in content.lower():
            print(f"yes python is present on line number : {i}")
        i+=1