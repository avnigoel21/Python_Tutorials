#Sets is a collection of non repetitive elements

# Sets are unordered => elements order doesnot matter
# Sets are unindexed = > cannot  access elements by index
# sets have no way to change the items
#sets cannot have duplicate values

# a = {1 , 2 , 4 , 7 , 1}

# print(type(a))
# print(a)


# empty set
# IMP : this syntax will create an empty dictionary and not an empty set
# b = {}
# print(type(b))
# # An empty set can be created using the below syntax:
c = set()
print(type(c))

# Adding values to an empty set
c.add(4)
c.add(5)
c.add(5)
c.add(5)
c.add(4)

c.add((3 , 4, 5)) # can add a tiple to a set
# c.add({4:5}) # Cannot add list or dictionary to sets
print(c)


# Sets methods/functions

# print(len(c)) # prints the length of this set


# c.remove(5) # removes 5 from the set c
# c.remove(15) # throws an error while trying to remove 15(which is not present in the set)
# print(c)


# c.pop() # removes an arbitary element from the set and returns the element removed
# print(c)


# c.clear() # Empty the set 
# print(c)





