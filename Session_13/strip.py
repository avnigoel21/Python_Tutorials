# this = "            Aditi is a good coder          "
# print(this)
# print(this.strip())

# Write a python function to remove a given word from a string and strip it at the same time.

def remove_and_split(string , word):
    newStr = string.replace(word , "")
    str = newStr.replace("  " , " ")
    return str.strip()


this = "            Aditi is a good coder          "
n = remove_and_split(this , "a")
print(n)
