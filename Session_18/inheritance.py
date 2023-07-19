#parent/base class
class Employee:
    company = "Google"

    def showDetails(self):
        print(f"This is an Employee")



# child class/derived class
class Programmer(Employee):
   # company = "Microsoft"
    language = "Python"

    def getLanguage(self):
        print(f"The language is {self.language}")

e = Employee()
p = Programmer()
p.showDetails()
print(p.company)
