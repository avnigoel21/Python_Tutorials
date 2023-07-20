# grand parent -> parent -> child

# grand parent
class Person:
    country = "India"

    def takeBreath(self):
        print("I am breathing")

# parent
class Employee(Person):
    company = "Honda"

    def takeBreath(self):
        print("I am an Employee , I am breathing")

#child
class Programmer(Employee):
    company = "Fiverr"

    def takeBreath(self):
        print("I am an Programmer , I am breathing")


p = Person()
p.takeBreath()
# print(p.company)  it will throw an error as company attribute is not present 

e = Employee()

pr = Programmer()
pr.takeBreath()
    
