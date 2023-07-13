# classes & objects

# class - is a blueprint/template for creating objects
# object - is an instantiation of a class

# Memory is allocated only after object instantiation

# blank form(class)  => fill by user => Application(object)
# class - variables & methods/functions



# Principles of OOPS
# 1) Abstraction  - our work is done without revealing the implementation details to the user
# 2) Encapsulation - binding 



# Modelling a program in OOPS

# Noun -> class -> Employee
# Adjective -> Attributes -> name , age , salary
# Verbs -> Methods -> getSalary() , increment()

# Class Attributes:
# An Attribute that belongs to the class rather than a particular object


# Instance Attributes / object attributes:
# An attribute that belongs to the instance (object) 

# aditi  and rohan attributes  -> 1) Is attributes present in object?
#                      2) Is attributes present in class?




class Number:
    def sum(self):
        return self.a + self.b
    

num = Number() # object instantiation
num.a = 12
num.b = 34
s = num.sum()
print(s)


# a = 12
# b = 34

# print("The sum of a and b is: " , a+b)


#camelCase - isFloatOrInt
#PascalCase - EmployeeName  - used in classes