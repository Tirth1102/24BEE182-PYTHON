xc = int(input("Enter x-coordinate of circle center: "))
yc = int(input("Enter y-coordinate of circle center: "))
r = int(input("Enter radius of the circle: "))
xp = int(input("Enter x-coordinate of point: "))
yp = int(input("Enter y-coordinate of point: "))
distance_squared = (xp - xc) * (xp - xc) + (yp - yc) * (yp - yc)
radius_squared = r * r
if distance_squared < radius_squared:
    print("Point is inside the circle")
elif distance_squared == radius_squared:
    print("Point is on the circle")
else:
    print("Point is outside the circle")

# Output:
# Enter x-coordinate of circle center: 2
# Enter y-coordinate of circle center: 5
# Enter radius of the circle: 3
# Enter x-coordinate of point: 0
# Enter y-coordinate of point: 3
# Point is inside the circle