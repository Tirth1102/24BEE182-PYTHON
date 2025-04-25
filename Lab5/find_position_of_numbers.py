numbers = [5, 12, 7, 12, 6, 12, 8, 3, 2, 12, 10, 1, 6, 9, 4, 12, 11, 15, 12, 14]
print(f"List: {numbers}")
target = int(input("Enter a number to find: "))
positions = []
for i in range(len(numbers)):
    if numbers[i] == target:
        positions.append(i)
print(f"Positions of {target}: {positions}\n")

# Output:
# List: [5, 12, 7, 12, 6, 12, 8, 3, 2, 12, 10, 1, 6, 9, 4, 12, 11, 15, 12, 14]
# Enter a number to find: 12
# Positions of 12: [1, 3, 5, 9, 15, 18]