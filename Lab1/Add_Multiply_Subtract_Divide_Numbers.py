a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

sum_result = a + b
sub_result = a - b
mul_result = a * b
if b != 0:
    div_result = a / b
else:
    div_result = "Invalid input."

print("Addition:", sum_result)
print("Subtraction:", sub_result)
print("Multiplication:", mul_result)
print("Division:", div_result)

# Output:
# Enter first number: 45
# Enter second number: 23
# Addition: 68.0
# Subtraction: 22.0
# Multiplication: 1035.0      
# Division: 1.9565217391304348