x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))
x3 = int(input("Enter x3: "))
y3 = int(input("Enter y3: "))
if (y2 - y1) * (x3 - x2) == (y3 - y2) * (x2 - x1):
    print("Points are on the same line")
else:
    print("Points are not on the same line")

# Output:
# Enter x1: 2
# Enter y1: 6
# Enter x2: 2
# Enter y2: 2
# Enter x3: 3
# Enter y3: 0
# Points are not on the same line