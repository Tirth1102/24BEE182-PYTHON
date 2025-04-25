data = ["Alice", ("Dev",), "Lila", ("Smit",), "Emma"]
boys = sum(1 for x in data if isinstance(x, tuple))
girls = sum(1 for x in data if not isinstance(x, tuple))
print("Number of boys:", boys)
print("Number of girls:", girls)

# Output:
# Number of boys: 2
# Number of girls: 3