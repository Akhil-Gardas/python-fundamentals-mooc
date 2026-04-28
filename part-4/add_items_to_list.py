num_items = int(input("How many items: "))
items = []

while len(items) < num_items:
    # Use len(items) + 1 to keep track of "Item 1", "Item 2", etc.
    value = int(input(f"Item {len(items) + 1}: "))
    items.append(value)

print(items)