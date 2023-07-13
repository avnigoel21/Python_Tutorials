class RailwayForm:
    formType = "RailwayForm"

    def printData(self):
        print(f"Name is {self.name}")
        print(f"Train is {self.train}")


aditiApplication = RailwayForm()

aditiApplication.name = "Aditi"
aditiApplication.train = "Rajdhani Express"

aditiApplication.printData()

