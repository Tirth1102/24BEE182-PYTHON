string = input("Enter a string: ")
alphabets = sum(c.isalpha() for c in string)
digits = sum(c.isdigit() for c in string)
print("Number of alphabets:", alphabets)
print("Number of digits:", digits)

# Output:
# Enter a string: computer
# Number of alphabets: 8
# Number of digits: 0