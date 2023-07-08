# Write a recursive function to calculate the sum of first n natural numbers


# 5 = 1 + 2 + 3 + 4 + 5 
n = 5

# sum = 0
# while(n > 0):
#     sum += n
#     n-=1
# print(sum)


def sum(n):
    if n == 1:
        return 1
    if n == 0:
        return 0
    else:
        return n+sum(n-1)
f = sum(n)
print(f)