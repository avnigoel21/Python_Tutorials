# more than one parent 

# 1st parent
class Employee:
    company = "Visa"
    eCode = 120

# 2nd parent
class Freelancer:
    company = "Fiverr"
    level = 0

    def upgradeLevel(self):
        self.level = self.level + 1

# child class
class Programmer(Employee , Freelancer):
    name = "Rohit"

p = Programmer()
# p.upgradeLevel()
# print(p.level)

print(p.company)

