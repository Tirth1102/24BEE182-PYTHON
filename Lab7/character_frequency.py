string = input("Enter a string: ")
char_freq = {}

for char in string:
    if char in char_freq:
        char_freq[char] += 1
    else:
        char_freq[char] = 1

print("Character Frequencies:")
print(char_freq)

# Output:
# Enter a string: MANAN
# Character Frequencies:  
# {'M': 1, 'A': 2, 'N': 2}