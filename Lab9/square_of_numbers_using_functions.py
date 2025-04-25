import random

random_numbers = random.sample(range(-15, 16), 10)  # 10 unique numbers
squared_numbers = [x**2 for x in random_numbers]

print("Random numbers:", random_numbers)
print("Squared numbers:", squared_numbers)

# Output:
# Random numbers: [10, 5, 12, 3, -3, 2, -11, 15, 8, 0]
# Squared numbers: [100, 25, 144, 9, 9, 4, 121, 225, 64, 0]