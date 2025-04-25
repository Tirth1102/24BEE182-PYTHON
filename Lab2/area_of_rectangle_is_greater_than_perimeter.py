length = int(input("Enter length of rectangle: "))
breadth = int(input("Enter breadth of rectangle: "))
area = length * breadth
perimeter = 2 * (length + breadth)
if area > perimeter:
    print("Area is greater than Perimeter")
else:
    print("Perimeter is greater than or equal to Area")

# Output:
# Enter length of rectangle: 10
# Enter breadth of rectangle: 10
# Area is greater than Perimeter