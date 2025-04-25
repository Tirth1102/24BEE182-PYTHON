fahrenheit = [32, 68, 77, 104]
celsius = []
for f in fahrenheit:
    c = (f - 32) * 5 / 9
    celsius.append(c)
print(f"Celsius: {celsius}\n")

# Output:
# Celsius: [0.0, 20.0, 25.0, 40.0]