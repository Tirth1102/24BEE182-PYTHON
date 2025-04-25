string1 = input("Enter first string: ")
string2 = input("Enter second string: ")

for i in range(len(string1) - len(string2) + 1):
    if string1[i:i+len(string2)] == string2:
        print("Yes, the second string is present in the first string.")
        break
else:
    print("No, the second string is not present in the first string.")

# Output:
# Enter first string: computer
# Enter second string: comp
# Yes, the second string is present in the first string.