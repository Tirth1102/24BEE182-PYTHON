num = int(input("Enter a number to check properties: "))
square = num * num
if str(square).endswith(str(num)):
    print(num, "is an Automorphic number")
else:
    print(num, "is not an Automorphic number")

# Output:
# Enter a number to check properties: 101
# 101 is not an Automorphic number