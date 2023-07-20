# It is used to access the methods of a super class in the derived class

# grand parent
class Person:
    country = "India"

    def __init__(self):
        print('Hi there')

    def takeBreath(self):
        print("I am breathing")

# parent
class Employee(Person):
    company = "Honda"

    def __init__(self):
        #super().__init__()
        print('Hi there , I am Employee')

    def takeBreath(self):
        super().takeBreath()
        print("I am an Employee , I am breathing")

#child
class Programmer(Employee):
    company = "Fiverr"

    def takeBreath(self):
        super().takeBreath()
        print("I am an Programmer , I am breathing")


p = Person()
# p.takeBreath()

e = Employee()

pr = Programmer()
# pr.takeBreath()
    
