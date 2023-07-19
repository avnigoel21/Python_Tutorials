# Can you change "self" parameter inside a class to something else (say mine). 
# Ans - yes

class Sample:

    # def __init__(self , name):
    #     self.name = name

    def __init__(sef , name):
        sef.name = name

obj = Sample("Aditi")
print(obj.name)
