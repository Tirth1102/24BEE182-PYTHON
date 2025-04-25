num = int(input("Enter a number to check properties: "))
sum_of_divisors = sum(i for i in range(1, num) if num % i == 0)
if sum_of_divisors == num:
    print(num, "is a Perfect number")
else:
    print(num, "is not a Perfect number")

# Output:
# Enter a number to check properties: 100
# 100 is not a Perfect number