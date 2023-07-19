# Create a class with a class attribute a ; create an object from it and set a directly 
# using object a = 0; Does this change the class attribute

# Ans  - No 

class Sample:
    a = "Aditi" # class attribute


obj = Sample()

# obj.a = "Vikky" 
Sample.a = "Rahul"

print(obj.a)
print(Sample.a)