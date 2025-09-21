# -----------------------------------------------------------------------------
# Description: Demonstrates methods for adding and removing elements from a list.
# -----------------------------------------------------------------------------

fruits = ["kiwi", "mango"]

# append(): Adds a single element to the end
fruits.append("orange")
print(f"After append(): {fruits}")

# insert(): Adds an element at a specified index
fruits.insert(0, "grape")
print(f"After insert(): {fruits}")

# extend(): Appends elements from another iterable
fruits.extend(["lemon", "lime"])
print(f"After extend(): {fruits}")

print("\n--- Removing Elements ---")

# remove(): Removes the first occurrence of a value
fruits.remove("mango")
print(f"After remove('mango'): {fruits}")

# pop(): Removes and returns the element at a specified index (or the last one)
popped_fruit = fruits.pop(1)
print(f"Popped element: {popped_fruit}")
print(f"After pop(1): {fruits}")

# del statement: Deletes an element at a specified index
del fruits[0]
print(f"After del fruits[0]: {fruits}")

# clear(): Removes all elements from the list
fruits.clear()
print(f"After clear(): {fruits}")
