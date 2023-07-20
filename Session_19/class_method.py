# A class method is a method which is bound to the class and not the object of the class 

class Employee:
    company = "Camel"
    salary = 100
    location = "Delhi"

    # def changeSalary(self , sal):
    #     self.__class__.salary = sal

    @classmethod # class method decorator is used to create a class method
    def changeSalary(cls , sal):
        cls.salary = sal


e = Employee()

print(e.salary)
e.changeSalary(500)
print(e.salary)
print(Employee.salary)

