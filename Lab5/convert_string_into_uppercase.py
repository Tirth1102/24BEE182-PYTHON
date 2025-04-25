strings = ["hello", "world", "openai", "python", "chat"]
uppercase = []
for s in strings:
    result = ""
    for c in s:
        if 'a' <= c <= 'z':
            result += chr(ord(c) - 32)
        else:
            result += c
    uppercase.append(result)
print(f"Uppercase: {uppercase}\n")

# Output:
# Uppercase: ['HELLO', 'WORLD', 'OPENAI', 'PYTHON', 'CHAT']