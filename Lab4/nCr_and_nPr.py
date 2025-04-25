n = int(input("Enter n: "))
r = int(input("Enter r: "))

fact_n = 1
for i in range(1, n + 1):
    fact_n *= i

fact_r = 1
for i in range(1, r + 1):
    fact_r *= i

fact_n_r = 1
for i in range(1, (n - r) + 1):
    fact_n_r *= i

nPr = fact_n // fact_n_r
nCr = fact_n // (fact_r * fact_n_r)

print("nPr:", nPr)
print("nCr:", nCr)

# Output:
# Enter n: 10
# Enter r: 2
# nPr: 90
# nCr: 45