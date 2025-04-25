names = set()

names.update(["Alice", "Bob", "Charlie", "David", "Eve"])
print("Set after adding names:", names)

if "David" in names:
    names.remove("David")
    names.add("Daniel")
print("Set after modifying 'David' to 'Daniel':", names)

names.discard("Alice")
names.discard("Bob")
print("Set after deleting 'Alice' and 'Bob':", names)

# Output:
# Set after adding names: {'Charlie', 'Eve', 'Bob', 'David', 'Alice'}
# Set after modifying 'David' to 'Daniel': {'Charlie', 'Eve', 'Daniel', 'Bob', 'Alice'}
# Set after deleting 'Alice' and 'Bob': {'Charlie', 'Eve', 'Daniel'}