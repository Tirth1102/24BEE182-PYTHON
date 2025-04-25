t = (10, 20, 30)
t = t[:1] + (99,) + t[2:] 
print("Modified tuple:", t)

# Output: 
# Modified tuple: (10, 99, 30)