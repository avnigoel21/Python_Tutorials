class Employee:
    company = "Google"
    salary  = 100

rohan = Employee()
aditi = Employee()


# aditi  and rohan attributes  -> 1) Is attributes present in object?
#                                 2) Is attributes present in class?
#                                 3) through an error


# creating instance attribute 'salary' for both the objects
rohan.salary = 300
aditi.salary = 400


print(rohan.salary)
print(aditi.salary)

# Throw an error as address is not present in instance/class
# print(aditi.address) 