bytes_size = float(input("Enter size in bytes: "))

kb = bytes_size / 1024
mb = kb / 1024
gb = mb / 1024

print("Size in KB:", kb)
print("Size in MB:", mb)
print("Size in GB:", gb)

# Output:
# Enter size in bytes: 1024
# Size in KB: 1.0
# Size in MB: 0.0009765625
# Size in GB: 9.5367431640625e-07