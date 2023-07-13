class Employee:
    company = "Google"

rohan = Employee()
aditi = Employee()

print(rohan.company)
print(aditi.company)

Employee.company = "YouTube"

print(rohan.company)
print(aditi.company)