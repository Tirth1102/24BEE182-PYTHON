def is_palindrome(string):
  string_len = len(string)
  for i in range(string_len // 2):
    if string[i] != string[string_len - i - 1]:
      return "The entered string is not a palindrome."
  return "The entered string is a palindrome."

a = input("Enter a string: ")
print(is_palindrome(a))

# Output:
# Enter a string: 12121
# The entered string is a palindrome.