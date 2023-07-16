# Create a class programmer for storing information of few programmers working at microsoft

class Programmer:
    company = "Microsoft" # class attribute

    def __init__(self , name , product):
        self.name = name
        self.product = product

    def getInfo(self):
        print(f"The name of programmer of company {self.company} is {self.name} and the product is {self.product}")

aditi = Programmer("Aditi" , "Github")
alka = Programmer("Alka" , "Skype")

aditi.getInfo()
alka.getInfo()



