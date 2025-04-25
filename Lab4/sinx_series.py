def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

def power(x, y):
    result = 1
    for _ in range(y):
        result *= x
    return result

def degrees_to_radians(degrees):
    pi = 3.141592653589793  
    return degrees * (pi / 180)

def sin_series(x, terms=10):
    x = degrees_to_radians(x) 
    sin_x = 0

    for n in range(terms):
        coefficient = (-1) ** n  
        numerator = power(x, 2 * n + 1)  
        denominator = factorial(2 * n + 1)  
        sin_x += coefficient * (numerator / denominator)

    return sin_x

x = float(input("Enter the value of x in degrees: "))
terms = int(input("Enter the number of terms in the series: "))

result = sin_series(x, terms)

print(f"sin({x}) ≈ {result}")

# Output:
# Enter the value of x in degrees: 30
# Enter the number of terms in the series: 3
# sin(30.0) ≈ 0.5000021325887924