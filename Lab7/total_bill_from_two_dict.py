prices = {'apple': 10, 'banana': 5, 'mango': 15}
quantities = {'apple': 2, 'banana': 6, 'mango': 3}

total = 0
for item in prices:
    if item in quantities:
        total += prices[item] * quantities[item]

print("Total Bill:", total)

# Output: 
# Total Bill: 105