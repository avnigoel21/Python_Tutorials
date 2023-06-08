#dictionary is a collection of key value pairs
# it is unorderd
# it is mutable
# cannot have duplicate keys


# myDict = {
#     "fast" : "In a quick manner" , 
#     "Aditi" : "A coder",
#     "Marks" : [1, 3, 5], 
#      1:2, 
#     "anotherDict" : {"Aditi" : "Dancer" , "Marks" : 78}
#     # "Aditi" : "A dancer", # override the previous key having same name
# }

# print(myDict['fast'])
# print(myDict['Aditi'])
# print(myDict[1])

# print(myDict["anotherDict"])
# print(myDict["anotherDict"]["Aditi"])

# myDict["Marks"] = [98 , 34]
# print(myDict)

#Dictionary Methods/functions

# print(list(myDict.keys())) # prints the keys of the dictionary
# print(myDict.values()) # prints thevalues of the dictionary
# print(myDict.items()) # rints the key , value for all the contents of the dict

# updateDict = {
#     "Science"  : "Subject" , 
#     "CS" : "subject"
# }
# myDict.update(updateDict) # Updates the dict by adding key-value pairs from updateDict
# print(myDict)


# print(myDict.get("Aditi2")) # Returns None as Aditi2 is not present in the dict
# print(myDict['Aditi2'])  # throws an error as Aditi2 is not present in the dict

