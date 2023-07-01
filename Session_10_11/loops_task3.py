# Write a program to find whether a given number is prime or not

num = int(input("Enter the number: "))

# num = 5
# 1 , 2 , 3 , 4, 5 => 1, 5 are factors i.e they are completely divisible by 5 i.e remainder is 0

prime = True

for i in range(2, num):
    if (num % i == 0):
        prime = False
        break;

if(prime):
    print("This number is Prime")
else:
    print("Not Prime")
