import random

numbers = {random.randint(15, 45) for _ in range(10)}
print("Original Set:", numbers)

count_less_than_30 = sum(1 for num in numbers if num < 30)
print("Count of numbers less than 30:", count_less_than_30)

numbers = {num for num in numbers if num <= 35}
print("Set after deleting numbers greater than 35:", numbers)

# Output:
# Original Set: {35, 38, 40, 16, 17, 20, 25, 27}
# Count of numbers less than 30: 5
# Set after deleting numbers greater than 35: {35, 16, 17, 20, 25, 27}