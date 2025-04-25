list1 = [1, 2, 3, 4, 5]
list2 = [2, 4, 6]
list3 = [x for x in list1 if x not in list2]
print(f"List1: {list1}")
print(f"List2: {list2}")
print(f"Items only in List1: {list3}")

# Output:
# List1: [1, 2, 3, 4, 5]
# List2: [2, 4, 6]
# Items only in List1: [1, 3, 5]