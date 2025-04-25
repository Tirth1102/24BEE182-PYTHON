N = int(input("Enter the number of terms: "))
a, b = 0, 1
for _ in range(N):
    print(a, end=" ")
    a, b = b, a + b

# Output: 
# Enter the number of terms: 10
# 0 1 1 2 3 5 8 13 21 34 