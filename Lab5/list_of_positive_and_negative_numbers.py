print("Separate positive and negative numbers:")
all_nums = [-10, -3, 4, -5, 6, 7, -2, 0, 8, 9, -1, -6, 2, 3, -4, 5, -8, -7, 1, 10, -9, -11, 11, 12, -12, 13, -13, 14, -14, 15]
pos = []
neg = []
for x in all_nums:
    if x > 0:
        pos.append(x)
    elif x < 0:
        neg.append(x)
print(f"Positive: {pos}")
print(f"Negative: {neg}\n")

# Output:
# Separate positive and negative numbers:
# Positive: [4, 6, 7, 8, 9, 2, 3, 5, 1, 10, 11, 12, 13, 14, 15]
# Negative: [-10, -3, -5, -2, -1, -6, -4, -8, -7, -9, -11, -12, -13, -14]