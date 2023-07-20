class Employee:
    company = " Google"

    salary = 5600
    salarybonus = 500
    #totalSalary = 6100

    @property
    def totalSalary(self):
        return self.salary + self.salarybonus


e = Employee()
print(e.totalSalary)