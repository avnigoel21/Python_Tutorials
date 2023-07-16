# Sometimes we need a function that doesn't use the self parameter, we can define a static method

class Employee:
    company = "Google"

    def getSalary(self, signature):
        print(f"Salary for this employee working in {self.company} is {self.salary} \n {signature}")

    @staticmethod #decorator to make greet() as a static method
    def greet():
        print("Good Morning, Sir")

    @staticmethod 
    def time():
        print("The time is 9AM in the morning")


rohan = Employee()

rohan.salary = 100000
rohan.getSalary("Thanks!") # Employee.getSalary(rohan)

rohan.greet()
rohan.time()