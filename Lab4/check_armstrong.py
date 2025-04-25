num = int(input("Enter a number to check properties: "))
temp = num
order = len(str(num))
sum_of_powers = sum(int(digit) ** order for digit in str(num))
if sum_of_powers == num:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")

# Output:
# Enter a number to check properties: 121
# 121 is not an Armstrong number 