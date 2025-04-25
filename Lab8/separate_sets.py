all_names = {"Alice", "Amanda", "Brian", "Brenda", "Albert", "Ben"}
set_a = {name for name in all_names if name.startswith("A")}
set_b = {name for name in all_names if name.startswith("B")}

print("Names starting with A:", set_a)
print("Names starting with B:", set_b)

# Output:
# Names starting with A: {'Alice', 'Amanda', 'Albert'}
# Names starting with B: {'Brian', 'Brenda', 'Ben'}