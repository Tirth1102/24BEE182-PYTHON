num = int(input("Enter a number (0-19): "))
num_words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
if 0 <= num <= 19:
    print(num_words[num])
else:
    print("Number out of range")

# Output:
# Enter a number (0-19): 15
# fifteen