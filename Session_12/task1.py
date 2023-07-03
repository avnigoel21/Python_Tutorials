# Write a program to calculate the factorial of a given number using for loop

# 5! = 1 x 2 x 3 x 4 x 5

# n! = 1 x 2 x 3 x 4 .....x n

# 0! = 1
# 1! = 1

num = int(input("Enter the number: "))

factorial = 1
for i in range(1 , num+1):
    factorial = factorial * i
print(f"The factorial of {num} is {factorial}")
print("The factorial of " + str(num) + " is " + str(factorial))