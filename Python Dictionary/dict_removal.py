# -----------------------------------------------------------------------------
# Description: Demonstrates methods for removing items from a dictionary.
# -----------------------------------------------------------------------------

shopping_cart = {
    "laptop": 1,
    "mouse": 2,
    "keyboard": 1,
    "monitor": 2
}

print(f"Original shopping cart: {shopping_cart}")

# The del statement removes an item by key.
del shopping_cart["mouse"]
print(f"After using del: {shopping_cart}")

# pop() removes an item by key and returns its value.
popped_value = shopping_cart.pop("keyboard")
print(f"Popped value: {popped_value}")
print(f"After pop(): {shopping_cart}")

# popitem() removes and returns the last key-value pair.
last_item = shopping_cart.popitem()
print(f"Removed with popitem(): {last_item}")
print(f"After popitem(): {shopping_cart}")

# clear() removes all items from the dictionary.
shopping_cart.clear()
print(f"After clear(): {shopping_cart}")
