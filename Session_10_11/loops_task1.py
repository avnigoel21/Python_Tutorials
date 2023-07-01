# Write a program to print multiplication table of a given number using for loop


# num = 3

# 3 x 1 = 3
# 3 x 2 = 6

num = int(input("Enter your number: "))

for i in range(1, 11):
    # print(str(num) +  " x " + str(i) + " = " + str(i * num))
    print(f"{num}x{i}={i*num}")      # f - strings


