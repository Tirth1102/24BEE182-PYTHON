t = (10, 20, 30, 40)
index_to_remove = 2
t = t[:index_to_remove] + t[index_to_remove + 1:]
print("Tuple after deletion:", t)

# Output:
# Tuple after deletion: (10, 20, 40)