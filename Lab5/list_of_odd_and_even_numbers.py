odd_list = [1, 3, 5, 7, 9]
even_list = [2, 4, 6, 8]
print(f"Original odd list: {odd_list}")
print(f"Original even list: {even_list}")
odd_list[2] = even_list[3]
print(f"Modified odd list: {odd_list}")
combined = odd_list + even_list
for i in range(len(combined)):
    for j in range(i + 1, len(combined)):
        if combined[i] > combined[j]:
            combined[i], combined[j] = combined[j], combined[i]
print(f"Sorted combined list: {combined}\n")

# Output:
# Original odd list: [1, 3, 5, 7, 9]
# Original even list: [2, 4, 6, 8]
# Modified odd list: [1, 3, 8, 7, 9]
# Sorted combined list: [1, 2, 3, 4, 6, 7, 8, 8, 9]