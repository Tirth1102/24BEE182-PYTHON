num = int(input("Enter a number to find factorial: "))
fact = 1
for i in range(1, num + 1):
    fact *= i
print("Factorial of", num, "is", fact)

# Output:
# Enter a number to find factorial: 10
# Factorial of 10 is 3628800