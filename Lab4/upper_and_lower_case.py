print("Uppercase alphabets:")
for char_code in range(ord('A'), ord('Z') + 1):
    print(chr(char_code), end=" ")
print()

print("\nLowercase alphabets:")
for char_code in range(ord('a'), ord('z') + 1):
    print(chr(char_code), end=" ")
print()

# Output:
# Uppercase alphabets:
# A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
# Lowercase alphabets:
# a b c d e f g h i j k l m n o p q r s t u v w x y z