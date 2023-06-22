# Write a program to input eight numbers from the user and display all the unique numbers (once)

# num1 = int(input("Enter number 1 : "))
# num2 = int(input("Enter number 2 : "))
# num3 = int(input("Enter number 3 : "))
# num4 = int(input("Enter number 4 : "))
# num5 = int(input("Enter number 5 : "))
# num6 = int(input("Enter number 6 : "))
# num7 = int(input("Enter number 7 : "))
# num8 = int(input("Enter number 8 : "))

# s = { num1 , num2 , num3 , num4 , num5 , num6 , num7 , num8 }
# print(s)

#------------------------------------------------------------------------------------------------

# Can we have a set with 18(int) and "18"(str) as a value in it.


# set = {18 , "18" , 18.9}
# print(set)
# print(len(set))

#-------------------------------------------------------------------------------------------------------


#  What will be the length of following set s:
# s = set()
# s.add(20)
# s.add(20.0)
# s.add("20")

# print(s)
# print(len(s))

#--------------------------------------------------------------------------------------------------

# Create an empty dictionary .
# Allow 4 friends to enter favourite language as values and use keys as their names.
# Assume that the names are unique

# favLang = {}
# a = input("Enter your favourte language Shubham : ")
# b = input("Enter your favourte language Ankit : ")
# c = input("Enter your favourte language Sonali : ")
# d = input("Enter your favourte language Harshita : ")

# favLang['Shubham'] = a
# favLang['Ankit'] = b
# favLang['Shubham'] = c
# favLang['Harshita'] = d

# print(favLang)

#-----------------------------------------------------------------------------------------------------------

# Can you change the values inside a list which is contained in set s

s = {8 , 7 , 12 , "aditi" , [1 , 2 , 5]}

#No we cannot update the list or chnge values inside a list because list is created inside the set which is hashable i.e non updatable

#---------------------------------------------------------------------------------------------------------------------



# Sets and tuples are hashable i.e non updateable once intialized
# Dictionary and lists are unhashable i.e  updateable after intialization

