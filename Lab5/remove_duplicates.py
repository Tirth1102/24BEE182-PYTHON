nums = [1, 5, 3, 1, 7, 5, 3, 9, 2, 1, 6, 7, 8, 5, 3, 2, 9, 1, 5, 3, 4, 6, 7, 8, 5, 3, 9, 0, 2, 3, 4, 5, 1, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 2, 1]
unique = []
for x in nums:
    if x not in unique:
        unique.append(x)
print(f"Unique values: {unique}\n")

# Output:
# Unique values: [1, 5, 3, 7, 9, 2, 6, 8, 4, 0]