# write a program to create a dictionary of hindi words with values as their english translation. 
# provide user an option to look it up.

myDictt = {
    "Pankha" : "Fan" ,
    "Dabba" : "box",
    "Vastu" : "Item"
}

a = input("Enter a hindi word : ")
print("The meaning of your word is : " , myDictt.get(a))



