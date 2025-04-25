main_string = input("Enter the main string: ")
remove_string = input("Enter the string to remove: ")
result = ""

i = 0
while i < len(main_string):
    if main_string[i:i+len(remove_string)] == remove_string:
        i += len(remove_string)  
    else:
        result += main_string[i]
        i += 1

print("Final string:", result)

# Output:
# Enter the main string: pythone
# Enter the string to remove: e
# Final string: python