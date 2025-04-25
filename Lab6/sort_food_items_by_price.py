food_items = [("Burger", 80), ("Pizza", 150), ("Fries", 60)]
sorted_items = sorted(food_items, key=lambda x: x[1], reverse=True)
print("Sorted food items:", sorted_items)

# Output:
# Sorted food items: [('Pizza', 150), ('Burger', 80), ('Fries', 60)]