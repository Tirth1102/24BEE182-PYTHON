string = input("Enter a string: ")
lowercase = ""
uppercase = ""
togglecase = ""

for char in string:
    if 'A' <= char <= 'Z':  
        lowercase += chr(ord(char) + 32)
        uppercase += char
        togglecase += chr(ord(char) + 32)
    elif 'a' <= char <= 'z':  
        lowercase += char
        uppercase += chr(ord(char) - 32)
        togglecase += chr(ord(char) - 32)
    else:
        lowercase += char
        uppercase += char
        togglecase += char

print("Lowercase:", lowercase)
print("Uppercase:", uppercase)
print("Toggle case:", togglecase)

# Output:
# Enter a string: Python
# Lowercase: python
# Uppercase: PYTHON
# Toggle case: pYTHON