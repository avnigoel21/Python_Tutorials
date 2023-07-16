# self refers to the instance/object of the class
# It is automatically passed with an function call from an object


class Employee:
    company = "Google"

    def getSalary(self):
        print(f"Salary for this employee working in {self.company} is {self.salary}")

rohan = Employee()
rohan.salary = 100000
rohan.getSalary() # Employee.getSalary(rohan)
