students = [(1, "John", 18), (2, "Alice", 19), (3, "Bob", 17)]
roll_nos = [s[0] for s in students]
names = [s[1] for s in students]
ages = [s[2] for s in students]
print("Roll numbers:", roll_nos)
print("Names:", names)
print("Ages:", ages)

# Output:
# Roll numbers: [1, 2, 3]
# Names: ['John', 'Alice', 'Bob']
# Ages: [18, 19, 17]