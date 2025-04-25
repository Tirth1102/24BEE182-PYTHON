num = int(input("Enter a number to check properties: "))
temp = 0
if num > 1:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            temp = 1
            break
if temp == 0 and num > 1:
    print(num, "is a Prime number")
else:
    print(num, "is not a Prime number")

# Output:
# Enter a number to check properties: 11
# 11 is a Prime number